
# def number():
#     num = input("Add number: ")

#     if len(num) != 5:
#         raise ValueError("Please add a number with exactly 5 digits")
    
#     # Виймемо першу, третю та п'яту цифри
#     digits = [int(num[0]), int(num[2]), int(num[4])]
#     # Виймемо другу та четверту цифри
#     digits2 = [int(num[1]), int(num[3])]
    
#     # Додаємо ці цифри
#     sum_of_digits = str(sum(digits)) + str(sum(digits2))

#     return sum_of_digits

# # Приклад використання
# print("Сума цифр:", number())



def number():
    num = input("Add number: ")

    if len(num) != 5:
        raise ValueError("Please add a number with exactly 5 digits")
    
    # Визначити суми цифр на парних і непарних позиціях
    sum_odd = sum(int(num[i]) for i in [0, 2, 4])
    sum_even = sum(int(num[i]) for i in [1, 3])
    
    # Конвертуємо суми у рядки і об'єднуємо
    result = str(sum_odd) + str(sum_even)

    return result

# # Приклад використання
print("Сума цифр:", number())

