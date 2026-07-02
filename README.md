# ML/MLOps Engineering Assessment

This repository contains a minimal, deterministic Python batch job for the Task 0 assessment.
It loads YAML config, reads OHLCV data from CSV, computes a rolling mean over `close`, generates a binary signal, writes metrics, and logs the run.

## What This Project Demonstrates

- Reproducibility through explicit config and seed handling.
- Observability through structured metrics and file-based logging.
- Deployment readiness through a Docker image that runs the job end to end.

## Repository Contents

- `run.py` - CLI entry point and orchestration.
- `validate_config.py` - YAML loading, validation, and seed setup.
- `validate_data.py` - CSV loading and dataset validation.
- `process_data.py` - rolling mean and signal generation.
- `metrics.py` - success and error metrics payloads.
- `logging_utils.py` - logger setup for `run.log`.
- `config.yaml` - required config values.
- `data.csv` - provided dataset.
- `requirements.txt` - Python dependencies.
- `Dockerfile` - container image definition.
- `README.md` - setup and execution instructions.

## Config

The required config file is `config.yaml` and must include:

```yaml
seed: 42
window: 5
version: "v1"
```

## Assessment Decisions

The implementation intentionally follows these choices:

- Default CLI arguments are supported so the script still runs when explicit paths are not passed.
- YAML is validated before use, including empty files, invalid syntax, and non-dictionary content.
- Validation checks values, not just key presence.
- The dataset is validated for readability, emptiness, invalid CSV structure, and the required `close` column.
- Column names are normalized before validation to reduce case-sensitivity issues.
- Configuration loading and dataset validation are separated so failures are easier to diagnose.
- A one-column CSV that actually contains comma-separated content is handled defensively.
- Rolling mean uses all available observations until the configured window is reached with `min_periods=1`.
- Metrics are produced for both success and error cases.

## Processing Logic

The job performs the following steps:

1. Load and validate YAML config.
2. Set the random seed from config.
3. Load and validate the input CSV.
4. Compute the rolling mean over `close` using the configured window.
5. Generate `signal = 1` when `close > rolling_mean`, otherwise `0`.
6. Measure total runtime in milliseconds.
7. Write metrics JSON to disk.
8. Write detailed logs to `run.log`.

The first `window - 1` rows are handled by partial-window rolling mean with `min_periods=1`.

## Required CLI

The assessment runner expects this exact command shape:

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

No hard-coded input or output paths are required. The defaults are present only as a convenience.

## Local Run

Install dependencies first:

```bash
pip install -r requirements.txt
```

Then run the job:

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

On success, the command writes `metrics.json` and `run.log` to the working directory and prints the metrics JSON to stdout.

## Docker Run

Build the image:

```bash
docker build -t mlops-task .
```

Run the container:

```bash
docker run --rm mlops-task
```

The container includes `data.csv` and `config.yaml`, runs the pipeline, writes `metrics.json` and `run.log`, and prints the final metrics JSON.

## Output Files

### `metrics.json`

Success output uses these keys:

```json
{
	"version": "v1",
	"rows_processed": 10000,
	"metric": "signal_rate",
	"value": 0.499,
	"latency_ms": 127,
	"seed": 42,
	"status": "success"
}
```

Error output uses this shape:

```json
{
	"version": "v1",
	"status": "error",
	"error_message": "Description of what went wrong"
}
```

The exact numeric values may vary slightly by environment, but the structure is deterministic.

### `run.log`

The log file includes:

- Job start timestamp.
- Config loaded and validated with seed, window, and version.
- Rows loaded.
- Rolling mean and signal generation steps.
- Metrics summary.
- Job end and status.
- Any validation errors or exceptions.

## Failure Behavior

The job writes an error metrics payload when validation or processing fails.
If the output file itself cannot be written, the process exits non-zero.

## Notes for Reviewers

- The program is designed to be deterministic for the same config and input data.
- The code favors explicit validation and straightforward error messages over implicit behavior.
- The Docker image uses `python:3.9-slim`, matching the suggested base image.
