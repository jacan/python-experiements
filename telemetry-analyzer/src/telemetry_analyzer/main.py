from rich import print
from pathlib import Path

from telemetry_analyzer.printer import (
    print_series_for_debug,
    print_series_for_debug
)

from telemetry_analyzer.parser import load_logs
from telemetry_analyzer.analyzer import (
    logs_to_data_frame,
    get_errors,
    count_errors_by_service,
    events_per_minute,
    rolling_error_count
)

def main():
    project_root = Path(__file__).parent.parent.parent
    log_path: Path = project_root / "sample_data" / "logs.json"
    logs = load_logs(log_path)

    dataframe = logs_to_data_frame(logs)
    errors = get_errors(dataframe)

    error_count = count_errors_by_service(dataframe)

    print(error_count)
    print(errors)
    print(dataframe.dtypes)

    # Time series..
    print("Time series:")
    events = events_per_minute(dataframe)

    print("Rolling Windows")
    error_window = rolling_error_count(dataframe)
    print_series_for_debug(error_window)


if __name__ == "__main__": main()