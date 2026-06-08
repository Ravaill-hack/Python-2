import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt


def print_graph(data_set: pd.DataFrame, campus: str):
    """
    A function that prints a graph of the life expectancy
    evolution related to a given country
    """
    sub_set = data_set.set_index("country")
    rows = sub_set.columns
    try:
        columns = sub_set.loc[campus]
        plt.plot(rows, columns, label=campus)
        plt.title(f"{campus} Life Expectancy Projections")
        plt.xlabel("Year")
        plt.xticks(rows[::40])
        plt.ylabel("Life expectancy")
        plt.yticks(range(30, 91, 10))
        plt.legend()
        plt.tight_layout()
        plt.show()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()
    except Exception as e:
        print(f"Exception: {e} is not a valid country name")
        exit()


def main():
    """
    A program that prints a graph of the life expectancy
    evolution in France
    """
    path = "life_expectancy_years.csv"
    campus = "France"
    data_set = load(path)

    print_graph(data_set, campus)


if __name__ == "__main__":
    main()
