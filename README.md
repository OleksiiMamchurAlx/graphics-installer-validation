# Graphics Package Diagnostics & Installer Validation

**QA / systems diagnostics case study · rollback · hash checks · synthetic measurements**

An independent, AI-assisted graphics R&D project raised a practical question: how can an experimental package be tested without confusing a successful installation with correct rendering or performance?

This repository presents sanitized installer-test evidence and a small offline measurement utility. **It contains no game files, graphics binaries or game-mod installer.**

## My contribution and AI assistance

Project owner; AI-assisted implementation, testing and documentation. I set the image-quality and performance goals, requested installation/rollback controls, and insisted on visible evidence and explicit unresolved results. AI assisted with diagnostics, scripts and documentation; upstream rendering technology is not my invention.

I use AI tools as engineering assistants. I define project goals, constraints and acceptance criteria, review outputs, preserve failures and limitations, and validate results through tests or reproducible evidence.

## Run the safe demo

Python 3.11 or newer; no additional packages, game installation, GPU or admin rights needed:

```console
python -m unittest discover -v
python frame_report.py fixtures/capture.synthetic.json
```

The fixture is artificial. Its calculated FPS is **not a game benchmark**. Base frame intervals, displayed frame intervals and latency are separate; missing latency stays `null`. The utility reads its input and prints JSON without changing the system.

## Installer validation evidence

The earlier private campaign ran these **four independent scenarios under two shell environments**: Windows PowerShell 5.1 and PowerShell 7. That is eight executions, not eight different cases.

| Scenario | Expected behavior | Earlier sandbox result |
|---|---|---|
| Normal profile install/restore | Preserve and restore originals | PASS in both shells |
| Split profile install/restore | Preserve and restore originals | PASS in both shells |
| Configuration changed after install | Refuse unsafe rollback | PASS in both shells |
| Payload hash mismatch | Stop before writing | PASS in both shells |

See [sanitized historical matrix](evidence/installer-matrix.json) and [current public-code tests](evidence/verification.json). The original installer is intentionally not redistributed; these installer results are historical records, not a claim that the new Python utility exercises the installer.

## A failure worth preserving

The first Windows PowerShell attempt failed because it inherited an incompatible module path. The fix changed the child process environment only, then repeated the tests in a fresh sandbox. A test environment failure was not recorded as a successful installer result or a live-game failure.

## Measurement discipline

For a future live A/B test, fix the scene, route, resolution, graphics settings and capture duration. Record base FPS, displayed FPS with frame generation, frametime distribution, latency and resource usage separately. Keep the original samples and run labels. Compare more than one run; screenshots of an FPS overlay alone are insufficient.

The project's 100+ displayed-FPS goal remains a **target**, not a verified final-build result. The included synthetic data must never be substituted for live captures.

## Limitations

- The sandbox matrix does not prove live-game stability, rendering quality or performance.
- This is not an official DLSS port, a new rendering engine or an NVIDIA-affiliated project.
- No present result establishes Windows reboot recovery or arbitrary crash-safe installation.
- No game is launched or modified by this repository.
- Frame-time calculations use the documented inverse-mean convention; they are not a substitute for capture-tool provenance or latency measurement.
- Only the new public Python utility and synthetic fixture are directly reproducible from this repository.

## Skills demonstrated

Test design, negative cases, compatibility analysis, rollback reasoning, hash-backed validation, Python measurement tooling, failure triage and honest engineering documentation.

[Rights and third-party boundaries](RIGHTS_AND_ATTRIBUTION.md) · [Publication manifest](PUBLICATION_MANIFEST.json)
