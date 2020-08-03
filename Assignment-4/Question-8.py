def prime(n):
    if n>1:
        for i in range(2,n):
            if n %i==0:
                print("Not Prime")
                break
            else:
                print("Prime Number")
    else:
        print("Not Prime")


if __name__ == '__main__':
    prime(int(input()))