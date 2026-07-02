# ML-OPS Assessment

This repository is a deterministic Python batch-processing assessment. The main entry point is `run.py`, which accepts a CSV input file, a YAML config file, and output paths for metrics and logs.

## Purpose

The project is intentionally small and explicit. It is meant to show basic MLOps-style engineering discipline rather than build a production trading system.

## Deliberate Decisions

The implementation choices behind this project are intentional and are part of the design:

- Default CLI arguments are provided so the program still works when the user does not pass paths explicitly.
- YAML is validated before use, instead of assuming the file is well formed.
- Validation checks the actual values, not just the presence of keys.
- Empty YAML files are rejected clearly.
- Non-dictionary YAML content is handled carefully, including a best-effort conversion when possible.
- The dataset is checked for emptiness and for header-only input before processing.
- Column names are normalized before validation so CSV variations are handled consistently.
- Configuration loading and dataset validation are separated into distinct error paths to make debugging easier.
- A single-column CSV with comma-separated values is handled more defensively.

## Behavior

The current code path is designed to:

- load configuration from YAML
- validate the required config keys: `seed`, `window`, and `version`
- validate config values before processing
- load OHLCV data from CSV
- validate the input data before processing
- compute a rolling mean over the `close` column
- generate binary trading signals
- write structured metrics to JSON
- write detailed execution logs

## Files

- `run.py` - command-line entry point
- `validate_config.py` - YAML loading and validation helper
- `config.yaml` - YAML configuration file
- `data.csv` - sample input data
- `requirements.txt` - Python dependencies
- `.gitignore` - local and generated file exclusions

## Setup

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

`config.yaml` must define these keys:

```yaml
seed: 42
window: 5
version: "1.0"
```

## Run

Use the default CLI shape:

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

Because default arguments are built in, the command can also be run without passing every flag explicitly.

## Outputs

The application is expected to produce:

- `metrics.json`
- `run.log`

These generated files are ignored by git so they do not get committed accidentally.
