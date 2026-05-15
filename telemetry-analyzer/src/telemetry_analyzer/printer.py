import pandas as pd

def print_series_for_debug(sr: pd.Series, message: str="Series:"):
    print(">-------------------------------------")
    print(message)
    print()
    print()
    print(sr)

def print_dataframe_for_debug(df: pd.DataFrame, message: str="DataFrame:"):
    print(">-------------------------------------")
    print()
    print()
    print(df)


