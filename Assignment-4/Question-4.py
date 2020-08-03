def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return "Perfect" if s==n else "Not Perfect"


if __name__ == '__main__':
    print(perfect(int(input())))