def bubble_sort(arr):
    s=True
    iteration = 0
    while(s):
        s = False
        for i in range(len(arr)-iteration-1):
            if arr[i]> arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                s=True
        iteration+=1
    return arr


if __name__ == '__main__':
    print(bubble_sort(list(map(int,input().split()))))