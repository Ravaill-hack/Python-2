import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        data_set = pd.read_csv(path)
        rows, columns = data_set.shape
        print(f"Loading dataset of dimensions ({rows}, {columns})")
        return (data_set)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
