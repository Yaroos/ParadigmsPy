

# Задача №1
# Дан список целых чисел numbers. Необходимо написать
# в императивном стиле
# процедуру для # сортировки числа в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки.
#
# алгоритм сортировки выбором



def selection_sort(numbers):
    num = len(numbers)
    for i in range(num):
        max_num = i
        for j in range(i + 1, num):
            if numbers[j] > numbers[max_num]:
                max_num = j
        numbers[i], numbers[max_num] = numbers[max_num], numbers[i]

numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print("Отсортированный список: ", numbers)