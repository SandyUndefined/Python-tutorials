import pandas as pd


def data():
    data = pd.read_csv('COVID Data.csv')
    gc = data.groupby(['State/UnionTerritory', 'Confirmed']).sum()
    print(gc)


if __name__ == '__main__':
    data()