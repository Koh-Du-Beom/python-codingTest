def parametric_search(arr):
    cur = -1
    step = len(arr)
    
    while step != 0:
        while (cur + step < len(arr)) and arr[cur + step] == True:
            cur += step
        step //= 2
    
    return cur

arr = [True, True, True, True, True, True, True, True, False, False, False, False]
print(parametric_search(arr))