if __name__ == '__main__':
    n = int(input())
    [print(i if n % i==0 else "") for i in range(1,n+1)]