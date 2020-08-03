def armstrong(n):
    s=0
    c=n
    if n >1000:
        return "Number greater than limit"
    else:
        while c>0:
            digit = c %10
            s+=digit**3
            c//=10
        return "Armstrong" if n==s else "Not Armstrong"


if __name__ == '__main__':
    print(armstrong(int(input())))