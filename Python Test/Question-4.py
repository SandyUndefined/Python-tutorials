from collections import Counter


def find(input_):
    wc = Counter(input_)
    s = max(wc.values())
    i = wc.values()
    print(wc.items())


if __name__ == "__main__":
   input_ = input()
   input_ = sorted(input_)
   find(input_)