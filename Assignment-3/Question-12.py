def fibbo(n):
    if n<=1:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)


if __name__ == '__main__':
    for _ in range(int(input())):
        print(fibbo(_))