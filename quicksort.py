def quick_sort(arr, low, high):
    if low < high:
        partition = partition_array(arr, low, high)
        quick_sort(arr, low, partition - 1)
        quick_sort(arr, partition + 1, high)

def partition_array(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, 5)

print(arr)
