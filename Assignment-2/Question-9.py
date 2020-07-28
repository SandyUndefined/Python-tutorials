if __name__ == '__main__':
    a = int(input())
    if a <=300:
        print(a*7)
    elif a <= 800:
        print((300*7)+(a -300)*9)
    elif a <=1500:
        print(((300*7)+(300 * 9)+ (a-300)*12))
    elif a>=1501:
        print(((300*7)+(300 * 9)+ (300 * 12)+(a-300)*15))