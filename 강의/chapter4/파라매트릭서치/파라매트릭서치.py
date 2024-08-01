def parametric_search(arr):
    ret = -1
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == True:
            left = mid + 1
            ret = mid
        else:
            right = mid + 1

    return ret

arr = [True, True, True, True, True, True, True, True, False, False, False, False]
print(parametric_search(arr))