def get_day_of_week(num):
    if num == 1:
        return "Понедельник"
    elif num == 2:
        return "Вторник"
    elif num == 3:
        return "Среда"
    elif num == 4:
        return "Четверг"
    elif num == 5:
        return "Пятница"
    elif num == 6:
        return "Суббота"
    elif num == 7:
        return "Воскресенье"
    else:
        return "Неверно, пожалуйста, введите число от 1 до 7"

num = int(input("Введите номер дня недели от 1 до 7: "))
result = get_day_of_week(num)
print(result)

