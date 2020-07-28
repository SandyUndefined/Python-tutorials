if __name__ == '__main__':
    x,y,z = map(int,input().split())
    if x==y==z:
        print("Equilateral")
    elif x==y or x==z or y==z:
        print("Isosceles")
    else:
        print("Scalene")