# Инверсия списка указывает, насколько далек список от сортировки.
# Инверсии - это пары элементов в списке, которые стоят не по порядку.
# Написать функцию count_inversions, которая определяет количество инверсий.
#
# Пример:
# [1, 3, 2, 4]  =>  1 инверсии: 2 и 3
# [4, 1, 2, 3]  =>  3 инверсии: 4 и 1, 4 и 2, 4 и 3


import traceback


def count_inversions(arr):
    # print(arr)
    counter = 0
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter = counter + 1

    return counter


# # Тесты
try:
    assert count_inversions([1, 2, 3]) == 0
    assert count_inversions([2, 1, 3]) == 1
    assert count_inversions([6, 5, 4, 3, 2, 1]) == 15
    assert count_inversions([6, 5, 4, 3, 3, 3, 3, 2, 1]) == 30
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
