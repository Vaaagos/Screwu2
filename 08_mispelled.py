# Напишите скрипт, который прверяет неправильное написание слов word1, word2:

# В результате получаем True, если word2 отличается от word1 не более чем на один символ.
# Если word2 отличается от word1 на два и более, то ответ False.
# Если в начале или в конце строки добавлен символ, то ответ True в том случае, если добвлено не больше однго символа!

# Например:
#   word1, word2 = 'versed', 'xersed' # returns True
#   word1, word2 = 'versed', 'v5rsed' # returns True
#   word1, word2 = 'versed', 'applb' # returns False
#   word1, word2 = '1versed', 'versed' # returns True
#   word1, word2 = 'versed', 'versed' # returns True
def check_spelling():
    # Вводим слова
    word1 = input("Первое слово: ")
    word2 = input("Второе слово: ")
    
    # Проверяем случай, когда слова совпадают
    if word1 == word2:
        return True
    
    # Проверяем случай, когда слова отличаются более чем на один символ
    if abs(len(word1) - len(word2)) >= 2:
        return False
    
    # Проверяем случай, когда слова отличаются на один символ
    if abs(len(word1) - len(word2)) == 1:
        if word1.startswith(word2) or word2.startswith(word1):
            return True
        if word1.endswith(word2) or word2.endswith(word1):
            return True
        return False
    
    # Проверяем случай, когда слова отличаются на один символ в середине
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False
    return True

