# Написать функцию remove_duplicate_words, которая оставляет в строке только уникльные слова.
#
# Пример:
# remove_duplicate_words("aaa bbb aaa bbb ccc aaa") ==> "aaa bbb ccc"

import traceback


def remove_duplicate_words(s):
    sarr = s.split(" ")
    answer = []
    result = ""
    index = 0
    for word in sarr:
        if index == 0:
            answer.append(word)
            result = word
        # if answer[len(answer) - 1] != word:
        if word not in answer:
            answer.append(word)
            result = result + " " + word
        index = index + 1
    return result


# Тесты
try:
    assert remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta") == "alpha beta gamma delta"
    assert remove_duplicate_words("my cat is my cat fat") == "my cat is fat"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")