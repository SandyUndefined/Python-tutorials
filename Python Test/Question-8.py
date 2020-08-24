import pandas as pd
import matplotlib.pyplot as plt


def show_graph():
    data = pd.read_csv('COVID Data.csv')
    s = data[['Selling Unit', 'Price']].plot(kind='bar', title='Bar Graph', figsize=(10, 10), legend=True, fontsize=12)
    s.set_xlabel("Price")
    s.set_ylabel("Selling Unit")
    plt.show()


if __name__ == '__main__':
    show_graph()