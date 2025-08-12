arr = [5, 2, 9, 1, 5, 6]

# сортировка списка (возвращает новый список)
sorted_arr = sorted(arr)
print(sorted_arr)

# сортировка списка на месте
arr.sort()
print(arr)



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))