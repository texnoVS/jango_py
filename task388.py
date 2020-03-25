# Написать функцию strong_enough(earthquake, age), которая вычисляет достаточно ли безопасное здание,
# чтобы выдержать землетрясение.  Здание рухнет, если сила землетрясения будет больше, чем сила здания.
# Earthquake – список, состоящий из спсика ударных волн.
# Вычисление силы землетрясения для [[5,3,7], [3,3,1], [4,1,2]]
# -> ((5 + 3 + 7) * (3 + 3 + 1) * (4 + 1 + 2)) = 735.
# Прочность нового здания 1000, при этом это значение уменьшается на 1% каждый год


import traceback


def strong_enough(earthquake, age):
    wava_summa = 0
    waves_result = 1
    strength = 1000
    for wave_data in earthquake:
        for number in wave_data:
            wava_summa = wava_summa + number
        if wava_summa != 0:
            # print(wava_summa)
            waves_result = waves_result * wava_summa
            # print(waves_result)
            wava_summa = 0

    strength = (strength / 100) * (100 - age)
    if strength < waves_result:
        return False
    else:
        return True


# strong_enough([[2,3,1],[3,1,1],[1,1,2]], 2)


# Тесты
try:
    assert strong_enough([[2,3,1],[3,1,1],[1,1,2]], 2) == True
    assert strong_enough([[5,8,7],[3,3,1],[4,1,2]], 2) == True
    assert strong_enough([[5,8,7],[3,3,1],[4,1,2]], 3) == False
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
