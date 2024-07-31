def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] < num:
            left = mid + 1
        
        if arr[mid] > num:
            right = mid - 1
        
        if arr[mid] == num:
            return mid
    
    return -1
