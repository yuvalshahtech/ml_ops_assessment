def build_success_metrics(processed_data, config, execution_latency):
    total_rows = len(processed_data)
    signal_rate = round(processed_data["signal"].mean(), 4)

    return {
        "version": config.get("version", "v1"),
        "rows_processed": total_rows,
        "metric": "signal_rate",
        "value":  signal_rate,
        "latency_ms": execution_latency,
        "seed": config.get("seed", None),
        "status": "success"
    }

def build_error_metrics(error_message, config=None):
    return {
        "version": config.get("version", "v1") if config else "v1",
        "status": "error",
        "error_message": error_message
    }