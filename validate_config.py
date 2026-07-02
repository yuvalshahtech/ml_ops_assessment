import numpy as np
import yaml

def load_and_validate_config(config_file):
    try:
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(
            f"Invalid YAML syntax in '{config_file}'. "
            f"Please check the file formatting.\n\n"
            f"Details:\n{e}"
        ) from e

    if config is None:
        raise ValueError(f"Config file '{config_file}' is empty.")

    if not isinstance(config, dict):
        try:
            config = dict(config)
        except (TypeError, ValueError):
            raise ValueError(
                f"Config file '{config_file}' must contain a dictionary. "
                f"Found {type(config).__name__}, and it could not be converted "
                f"into a valid dictionary."
            )

        if not isinstance(config, dict):
            raise ValueError(
                f"Config file '{config_file}' could not be converted into a valid dictionary."
            )

    required_fields = ["seed", "window", "version"]
    for field in required_fields:
        if field not in config:
            raise ValueError(
                f"Missing required field '{field}' in config file."
            )

    if not isinstance(config["seed"], int):
        raise ValueError(
            f"'seed' must be an integer. Found {type(config['seed']).__name__}."
        )

    if not isinstance(config["window"], int) or config["window"] <= 0:
        raise ValueError(
            "'window' must be a positive integer."
        )

    if not isinstance(config["version"], (str, int, float)):
        raise ValueError(
            "'version' must be a string, integer, or float."
        )

    np.random.seed(config["seed"])

    return config