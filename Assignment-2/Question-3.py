if __name__ == '__main__':
    x,y = map(int,input().split())
    o = input()
    if o =='+':
        print(x+y)
    elif o== '-':
        print(abs(x-y))
    elif o=='*':
        print(x*y)
    elif o=='/':
        print(x/y)
    else:
        print("enter + , - ,* or / only")