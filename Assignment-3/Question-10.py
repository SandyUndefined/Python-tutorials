if __name__ == '__main__':
    n = int(input())
    k = 0
    for i in range(n + 1):
        for j in range(i):
            print("*", end=' ')
        print("")
    print("----------------------")
    for i in range(n, 0, -1):
        k += 1
        for j in range(1, i + 1):
            print("*", end=' ')

        print('')
