import json
from pathlib import Path

from telemetry_analyzer.models import LogEntry

def load_logs(path: Path) -> list[LogEntry]:
    """

    :rtype: list[LogEntry]
    """
    with open(path, "r") as file:
        data = json.load(file)
    return [LogEntry(**entry) for entry in data]