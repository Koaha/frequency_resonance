# Developer Documentation — Frequency Resonance Pipeline

This folder contains technical documentation for developers working on the
frequency_resonance signal processing pipeline.  It is separate from the
user-facing `README.md` and focuses on algorithmic design, API contracts,
and configuration internals.

---

## Contents

| Document | What it covers |
|---|---|
| [robust_sqi_design.md](robust_sqi_design.md) | Full algorithmic design of the robust scale-agnostic SQI scorer — motivation, theory, decision tree, edge cases, limitations |
| [api_reference.md](api_reference.md) | API contracts for `RobustConfig`, `FileQualityRegime`, `robust_score_windows()`, and `SignalProcessor.compute_robust_sqi()` |
| [config_reference.md](config_reference.md) | Every `robust_composite:` YAML key — type, default, valid range, and effect on behaviour |

---

## Quick orientation

The SQI scoring pipeline has three modes, selected via `threshold_method` in `config.yaml`:

```
threshold_method: value            ← legacy: single metric + hard cutoff
threshold_method: composite        ← legacy: weighted 5-feature composite
threshold_method: robust_composite ← recommended: rank-based, scale-agnostic
```

The robust scorer is implemented in:
- `src/core/signal_processing/sqi_scorer.py`  — core algorithm
- `src/core/signal_processing/signal_processor.py`  — `compute_robust_sqi()` method
- `src/core/signal_processing/config.py`  — `RobustConfig` dataclass + YAML parsing
- `config.yaml`  — `robust_composite:` section

Start with [robust_sqi_design.md](robust_sqi_design.md) for the conceptual picture,
then [api_reference.md](api_reference.md) for function signatures, and
[config_reference.md](config_reference.md) for tuning.
