import argparse
import os
import sys
from metrics import build_error_metrics, build_success_metrics
from process_data import process_data
from validate_config import load_and_validate_config
from validate_data import load_and_validate_data
import time
import json

def format_error(e):
    return str(e)

def main():
    start_time = time.perf_counter()
    config = None
    metrics = None

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data.csv")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--output", default="metrics.json")
    parser.add_argument("--log-file", default="run.log")
    args = parser.parse_args()

    input_file = args.input
    config_file = args.config
    output_file = args.output
    log_file = args.log_file

    try:
        config = load_and_validate_config(config_file)
        data = load_and_validate_data(input_file)
        processed_data = process_data(data, config["window"])
        end_time = time.perf_counter()
        execution_latency = round((end_time - start_time) * 1000)
        metrics = build_success_metrics(
            processed_data,
            config,
            execution_latency
        )
    except Exception as e:
        metrics = build_error_metrics(format_error(e), config)
        sys.exit(1)
    try:
        with open(output_file, "w") as f:
            json.dump(metrics, f, indent=4)
    except Exception as e:
        print(f"Error writing metrics to file: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()