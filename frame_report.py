"""Offline interval analysis. Synthetic measurements must remain labelled synthetic."""
import argparse
import json
import math
import statistics
from pathlib import Path

def metrics(values):
    if not isinstance(values, list) or not values:
        raise ValueError('Non-empty list of intervals required')
    if any(type(x) not in (int, float) or not math.isfinite(x) or x <= 0 for x in values):
        raise ValueError('Intervals must be positive finite milliseconds')
    slowest = sorted(values, reverse=True)[:max(1, math.ceil(len(values) * .01))]
    return {'mean_fps': 1000 / statistics.mean(values),
            'one_percent_low_fps': 1000 / statistics.mean(slowest), 'frames': len(values)}

def report(data):
    if data.get('mode') not in ('SYNTHETIC', 'MEASURED'):
        raise ValueError('Explicit SYNTHETIC or MEASURED provenance required')
    latency = data.get('latency_ms')
    if latency is not None and (type(latency) not in (int, float) or not math.isfinite(latency) or latency < 0):
        raise ValueError('Latency must be a non-negative finite number or null')
    return {'mode': data['mode'],
            'base': metrics(data['base_intervals_ms']) if data.get('base_intervals_ms') is not None else None,
            'displayed': metrics(data['display_intervals_ms']) if data.get('display_intervals_ms') is not None else None,
            'latency_ms': latency,
            'method': 'FPS = 1000/mean interval. 1% low = 1000/mean slowest ceil(N*0.01) intervals.',
            'limitation': 'No base FPS inferred from frame generation; input provenance is supplied, not independently authenticated.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('capture', type=Path)
    args = parser.parse_args()
    print(json.dumps(report(json.loads(args.capture.read_text(encoding='utf-8'))), indent=2, allow_nan=False))
