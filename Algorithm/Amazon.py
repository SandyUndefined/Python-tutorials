'''
Given an array nums you need to find sum of the k elements such that it's maximum
Input : [80,-50,90,100]
    k = 2
Output : 190
'''


def maxi(arr, k):
    new = 0
    for i in range(k):
        new += arr[i]

    curr_sum = new
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i - k]
        new = max(new, curr_sum)
    print(new)


if __name__ == '__main__':
    n = list(map(int, input().split()))
    k = int(input())
    maxi(n, k)
