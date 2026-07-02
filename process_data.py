import pandas as pd

def compute_rolling_mean(data, window):
    """
    Compute the rolling mean for the 'close' column using the specified window size.
    For the initial rows where the full window size is not available, compute the mean
    using all available historical rows (partial-window rolling mean).

    Parameters:
    data (pd.DataFrame): The input DataFrame containing a 'close' column.
    window (int): The window size for computing the rolling mean.

    Returns:
    pd.Series: Rolling mean of the 'close' column.
    """
    close = pd.to_numeric(data["close"], errors="raise")
    return close.rolling(window=window, min_periods=1).mean()


def process_data(data, window):
    """
    Process the input DataFrame by computing the rolling mean and generating a binary signal.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing a 'close' column.
    window (int): The window size for computing the rolling mean.

    Returns:
    pd.DataFrame: The updated DataFrame with the rolling mean and binary signal columns.
    """
    processed_data = data.copy()

    close = pd.to_numeric(processed_data["close"], errors="raise")
    rolling_mean = compute_rolling_mean(processed_data, window)
    signal = (close > rolling_mean).astype(int)

    processed_data["rolling_mean"] = rolling_mean
    processed_data["signal"] = signal

    return processed_data