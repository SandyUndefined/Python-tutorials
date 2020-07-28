if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        if i >1:
            for j in range(2,i//2+2):
                if i %j ==0:
                    break
                else:
                    if j==i//2+1:
                        print(i)