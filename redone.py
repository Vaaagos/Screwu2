# Переделал решение без функции
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if len(set(word1) - set(word2)) <= 1:
    print(True)
else:
    print(False)
# Вроде так)