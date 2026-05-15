import pandas as pd

from telemetry_analyzer.models import LogEntry

def logs_to_data_frame(logs: list[LogEntry]) -> pd.DataFrame:
    return pd.DataFrame(log.model_dump() for log in logs)

def get_errors(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["level"] == "ERROR"]

def count_errors_by_service(df: pd.DataFrame) -> pd.Series:
    errors = df[df["level"] == "ERROR"]

    return errors.groupby("service").size()

def sort_by_timestamp(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by="timestamp", ascending=False)

def events_per_service(df: pd.DataFrame) -> pd.Series:
    return df.groupby("service").size()

def events_per_minute(df: pd.DataFrame) -> pd.Series:
    return df.set_index("timestamp").resample("1min").size()

def rolling_error_count(df: pd.DataFrame) -> pd.Series:
    errors = df[df["level"] == "ERROR"]

    return (
        errors
        .set_index("timestamp")
        .resample("1min")
        .size()
        .rolling(window=3)
        .mean()
    )