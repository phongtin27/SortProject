import time
fi = open('TEST 10')
def MergeSort(arr,l,r):
    if l==r:
        return
    mid = (l+r)//2
    MergeSort(arr,l,mid)
    MergeSort(arr,mid+1,r)
    Contain = []
    i,j =l,mid+1
    while i<=mid and j<=r:
        if arr[i] < arr[j]:
           Contain.append(arr[i])
           i += 1 
        else:
            Contain.append(arr[j])
            j += 1
    while i<=mid:
        Contain.append(arr[i])
        i+=1
    while j<=r:
        Contain.append(arr[j])
        j+=1
    for i in range(l,r+1):
        arr[i] = Contain[i-l]
# in ra thời gian chạy của hàm Heapsort
def Findtime(arr):
    start = time.perf_counter()
    MergeSort(arr,0,len(arr)-1)
    end = time.perf_counter()
    print(f"Thời gian chạy: {end - start:.6f} giây")
s = int(fi.readline())
a = list(map(float,fi.readline().split()))
Findtime(a)