if __name__ == '__main__':
    a,b,c,d,e = map(int,input().split())
    x= (a+b+c+d+e)/5
    if x>=90:
        print("o")
    elif 80 <= x <= 89:
        print("E")
    elif 70 <= x <= 79:
        print("A")
    elif x < 70:
        print("B")