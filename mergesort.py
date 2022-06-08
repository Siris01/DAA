def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_arr = arr[left: mid + 1]
    right_arr = arr[mid + 1: right + 1]
    
    left_arr.append(float('inf'))
    right_arr.append(float('inf'))

    i = j = 0
    for k in range(left, right + 1):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1

arr = [10, 7, 8, 9, 1, 5]
merge_sort(arr, 0, 5)
print(arr)