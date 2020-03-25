# Написать функцию palindrom, которая определяет является ли заданное число палиндромом
# (читается одинаково слева направо и справа налево)
#
# Пример:
# palindrom(1234321) ==> True

import traceback


def palindrom(number):
    slovo = str(number)
    x = len(slovo)
    i = 0
    x = x - 1
    k = 0
    while x - i >= i:
        if slovo[x - i] == slovo[i]:
            i += 1
        else:
            k = 1
            break
    if k == 1:
        return False
    else:
        return True

#Тесты
try:
    assert palindrom(0) == True
    assert palindrom(1233221) == False
    assert palindrom(1000010) == False
    assert palindrom(5555555) == True
    assert palindrom(1234554321) == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")