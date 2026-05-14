from rich import print
from pathlib import Path

from telemetry_analyzer.parser import load_logs
from telemetry_analyzer.analyzer import (
    logs_to_data_frame,
    get_errors
)

def main():
    project_root = Path(__file__).parent.parent.parent
    log_path: Path = project_root / "sample_data" / "logs.json"
    logs = load_logs(log_path)

    dataframe = logs_to_data_frame(logs)
    errors = get_errors(dataframe)

    print(errors)

if __name__ == "__main__": main()