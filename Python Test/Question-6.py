import pandas as pd


def data():
    data = pd.read_csv('Price vs selling unit.csv')
    print(len(data))


if __name__ == '__main__':
    data()