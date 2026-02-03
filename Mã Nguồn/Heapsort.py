import time
fi = open('TEST 10')
def heapify(arr,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l 
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)
def Heapsort(arr,n):
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
# in ra thời gian chạy của hàm Heapsort
def Findtime(arr):
    start = time.perf_counter()
    Heapsort(arr,len(arr))
    end = time.perf_counter()
    print(f"Thời gian chạy: {end - start:.6f} giây")
s = int(fi.readline())
a = list(map(float,fi.readline().split()))
Findtime(a)