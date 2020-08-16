def main():
    n = int(input())
    arr = list(map(int, input().split()))

    avg = sum(arr) // n
    b = [0] * n
    for i in range(n - 1):
        b[i + 1] = b[i] + arr[i] - avg
    b = sorted(b)
    med = -b[n // 2]
    ans = 0
    for i in range(n):
        ans += abs(med + b[i])
    print(ans)


if __name__ == '__main__':
    main()