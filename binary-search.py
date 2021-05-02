# prerequisit - Array must be sorted


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = (low + high)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        print(mid)
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            return binary_search_recursive(arr, target, low, mid-1)
        else:
            return binary_search_recursive(arr, target, mid+1, high)


bs = binary_search_recursive([2, 4, 5, 7, 8, 9, 12, 14, 16, 21], 16, 0, 9)
print(bs)
