import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt


def clean_number(raw_number: str) -> float:
    """
    A function that removes the suffixes "M" and "k"
    and converts the string numbers to floats
    """
    if raw_number.endswith("M"):
        return float(raw_number[:-1]) * 1e6
    elif raw_number.endswith("k"):
        return float(raw_number[:-1]) * 1e3
    else:
        return float(raw_number)


def print_graph(data_set: pd.DataFrame, country1: str, country2: str):
    """
    A function that prints a graph of the life expectancy
    evolution related to a given country
    """
    sub_set = data_set.set_index("country")
    rows = sub_set.columns.astype(int)
    try:
        raw_columns1 = sub_set.loc[country1]
        columns1 = [clean_number(numbers) for numbers in raw_columns1]
        raw_columns2 = sub_set.loc[country2]
        columns2 = [clean_number(numbers) for numbers in raw_columns2]

        plt.plot(rows, columns1, label=country1)
        plt.plot(rows, columns2, label=country2)
        plt.title("Population Projections")

        plt.xlabel("Year")
        plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
        plt.xlim(1800, 2050)

        plt.ylabel("Population")
        max_pop = max(max(columns1), max(columns2))
        y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

        plt.legend(loc="lower right")
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
    A program that prints a graph of comparative
    data between France and United Kingdom
    """
    path = "population_total.csv"
    campus1 = "France"
    campus2 = "Belgium"
    data_set = load(path)

    print_graph(data_set, campus1, campus2)


if __name__ == "__main__":
    main()
