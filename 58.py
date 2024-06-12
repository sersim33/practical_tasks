
def segment_count_and_remainder(a, b):
    """
    Функція для обчислення кількості відрізків b, які можуть бути розміщені на відрізку a,
    і довжини незайнятої частини на відрізку a.
    """
    count_b = a // b
    rest_a = a % b
    
    return count_b, rest_a

# Тестові дані
a = 10098
b = 191

# Викликаємо функцію і отримуємо результат
result = segment_count_and_remainder(a, b)

# Виводимо результат
print(result)
