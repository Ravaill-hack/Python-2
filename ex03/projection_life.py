import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt


def print_graph(incomes_data: pd.DataFrame, life_data: pd.DataFrame):
    """
    A function that print scatters of data
    """

    try:
        GNP_1900 = incomes_data["1900"].astype(int)
        life_1900 = life_data["1900"]

        plt.figure(figsize=(10, 8))
        plt.scatter(GNP_1900, life_1900)

        plt.title("1900")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.xlabel("Gross domestic product")

        plt.ylabel("Life Expectancy")
        plt.show()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()
    except Exception as e:
        print(f"Exception: {e}")
        exit()


def main():
    """
    A program that displays the projection of life expectancy in relation
    to the gross national product of the year 1900 for each country
    """
    incomes_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_path = "life_expectancy_years.csv"
    incomes_data = load(incomes_path)
    life_data = load(life_path)

    print_graph(incomes_data, life_data)


if __name__ == "__main__":
    main()
