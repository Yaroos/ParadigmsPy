def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [2, 3, 4, 10, 40]
x = int(input("Введите число: "))
result = binary_search(arr, x)
if result != -1:
    print("Элемент найден в индексе", result)
else:
    print("Элемент не найден в массиве")