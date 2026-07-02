import argparse
import os
import sys
from validate_config import load_and_validate_config
from validate_data import load_and_validate_data

def main():
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

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    if not os.path.exists(config_file):
        print(f"Error: Config file '{config_file}' does not exist.")
        return
    try:
        config = load_and_validate_config(config_file)
    except ValueError as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)
    try:
        data = load_and_validate_data(input_file)
    except ValueError as e:
        print(f"Data Validation Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)

    print(f"Input value: {input_file}")
    print(f"Config value: {config_file}")
    print(f"Output value: {output_file}")
    print(f"Log file value: {log_file}")
    print(f"Config contents: {config}")
    print(f"Data contents: {data.head()}")  # Print first few rows of the data

if __name__ == "__main__":
    main()