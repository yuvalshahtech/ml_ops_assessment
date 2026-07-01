import argparse
import os

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

    # Edge case handling

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    if not os.path.exists(config_file):
        print(f"Error: Config file '{config_file}' does not exist.")
        return

    print(f"Input value: {input_file}")
    print(f"Config value: {config_file}")
    print(f"Output value: {output_file}")
    print(f"Log file value: {log_file}")

if __name__ == "__main__":
    main()