if __name__ == '__main__':
    n = int(input())
    k=(2*n)-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k-=1
        for j in range(i+1):
            print("0",end=' ')
        print(" ")
    print("-------------------")
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k += 1
        for j in range(0, i + 1):
            print("0", end=" ")
        print("")