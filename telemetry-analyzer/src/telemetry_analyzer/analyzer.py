import pandas as pd

from telemetry_analyzer.models import LogEntry

def logs_to_data_frame(logs: list[LogEntry]) -> pd.DataFrame:
    return pd.DataFrame(log.model_dump() for log in logs)

def get_errors(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["level"] == "ERROR"]

def count_errors_by_service(df: pd.DataFrame) -> pd.Series:
    errors = df[df["level"] == "ERROR"]

    return errors.groupby("service").size()
