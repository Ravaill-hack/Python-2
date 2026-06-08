import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    A function that loads a .csv file and returns a DataFrame
    """
    try:
        data_set = pd.read_csv(path)
        rows, columns = data_set.shape
        print(f"Loading dataset of dimensions ({rows}, {columns})")
        return (data_set)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()
    except Exception as e:
        print(f"Exception: {e}")
        exit()
