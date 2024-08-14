def binary_search(arr, num):
    cur = -1
    step = len(arr)
    
    while step != 0:
        while cur + step < len(arr) and arr[cur + step] <= num:
            cur += step
        step //= 2
    
    return cur
 