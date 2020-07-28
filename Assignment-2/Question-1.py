if __name__ == '__main__':
    a,b,c,d = map(int,input().split())
    print("Passed" if (a+b+c+d)/4 > 33.0 else "Failed")