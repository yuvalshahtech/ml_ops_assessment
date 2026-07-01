# COPILOT.md

# ML/MLOps Internship Assessment

This repository is a technical assessment for an ML/MLOps Engineering Internship.

The goal is NOT to build a production trading system.

The goal is to demonstrate software engineering skills commonly expected from an ML Engineer.

## Primary Objective

Build a small, deterministic batch-processing application in Python that:

- Reads configuration from YAML
- Reads OHLCV data from CSV
- Computes a rolling mean on the `close` column
- Generates binary trading signals
- Produces structured metrics as JSON
- Produces detailed logs
- Runs both locally and inside Docker

Everything should be deterministic and reproducible.

---

# IMPORTANT

Do NOT invent additional requirements.

Only implement what is explicitly required by the assessment.

Avoid overengineering.

Keep the code clean, modular, and easy to understand.

---

# Required CLI

The application must support:

python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log

Do not hardcode any file paths.

---

# Required Files

run.py

config.yaml

data.csv

requirements.txt

Dockerfile

README.md

metrics.json

run.log

---

# Functional Requirements

## Config

Load YAML configuration.

Required keys:

- seed
- window
- version

Validate all required keys before processing.

Set NumPy random seed.

---

## Dataset

Load CSV.

Validate:

- file exists
- readable CSV
- non-empty
- contains "close" column

Handle failures gracefully.

---

## Processing

1. Load config
2. Validate config
3. Load CSV
4. Validate CSV
5. Compute rolling mean
6. Generate binary signals
7. Compute metrics
8. Write metrics.json
9. Write run.log

---

# Metrics JSON

Must always be produced.

Success:

- version
- rows_processed
- metric
- value
- latency_ms
- seed
- status

Error:

- version
- status
- error_message

Even on failure, metrics.json must exist.

---

# Logging

Log:

- Job start
- Config loaded
- Validation
- Rows loaded
- Rolling mean
- Signal generation
- Metrics
- Job completion
- Errors

Use Python logging.

---

# Docker

The Docker image must:

- build successfully
- run successfully
- include config.yaml
- include data.csv
- produce metrics.json
- produce run.log
- print metrics.json to stdout

---

# Coding Style

Prefer:

- small functions
- clear variable names
- explicit validation
- descriptive error messages

Avoid:

- giant functions
- duplicated logic
- unnecessary abstraction
- premature optimization

---

# Decision Rule

If uncertain whether to implement something:

Follow the assessment specification.

Do not assume additional business logic.

---

# Assistant Behaviour

When suggesting code:

1. Explain WHY.
2. Explain WHAT problem it solves.
3. Keep changes minimal.
4. Preserve deterministic behaviour.
5. Never remove required functionality.

Always prioritize correctness over cleverness.