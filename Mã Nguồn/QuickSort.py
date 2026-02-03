import time
import random 
fi = open('TEST 10')
def Quicksort(arr,l,r):
    if l>=r:
        return
    privot = random.randint(l,r)
    a[privot],a[l] = a[l],a[privot]
    privot = a[l]
    j = l-1
    for i in range(l,r+1):
        if arr[i] < privot:
            j += 1
            arr[j],arr[i] = arr[i],arr[j]
    if j < l:
        j += 1
    Quicksort(arr,l,j)
    Quicksort(arr,j+1,r)
    return

# in ra thời gian chạy của hàm Quicksort
def Findtime(arr):
    start = time.perf_counter()
    Quicksort(arr,0,len(arr)-1)
    end = time.perf_counter()
    print(f"Thời gian chạy: {end - start:.6f} giây")
s = int(fi.readline())
a = list(map(float,fi.readline().split()))
Findtime(a)