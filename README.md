# ML-OPS Assessment

This repository is a small, deterministic Python batch-processing assessment. The main entry point is `run.py`, which accepts a CSV input file, a YAML config file, and output paths for metrics and logs.

## What it does

The project is designed to:

- load configuration from YAML
- validate the required config keys: `seed`, `window`, and `version`
- load OHLCV data from CSV
- validate the input data before processing
- compute a rolling mean over the `close` column
- generate binary trading signals
- write structured metrics to JSON
- write detailed execution logs

## Files

- `run.py` - command-line entry point
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

Use the required CLI shape:

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

## Outputs

The application is expected to produce:

- `metrics.json`
- `run.log`

These generated files are ignored by git so they do not get committed accidentally.
