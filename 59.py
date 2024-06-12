def digit_sum(number):
    """
    Функція для обчислення суми цифр числа.
    
    :param number: Число.
    :return: Сума цифр числа.
    """
    # Перетворюємо число на рядок для зручності обробки кожної цифри окремо
    number_str = str(number)
    
    # Ініціалізуємо змінну для суми цифр
    total_sum = 0
    
    # Ітеруємося по кожному символу у рядку та додаємо його до суми
    for digit in number_str:
        total_sum += int(digit)
    
    return total_sum

# Тестові дані
number = 999

# Викликаємо функцію і отримуємо результат
result = digit_sum(number)
# Виводимо результат
print(result)

            #або такий варіант:

def digit_sum(number):
    """
    Функція для обчислення суми цифр числа за допомогою спискового виразу.
    
    :param number: Число.
    :return: Сума цифр числа.
    """
    # Розбиваємо число на цифри, перетворюючи його на рядок, а потім на список цифр
    digits = [int(digit) for digit in str(number)]
    
    # Обчислюємо суму цифр
    total_sum = sum(digits)
    
    return total_sum

# Тестові дані
number = 12345

# Викликаємо функцію і отримуємо результат
result = digit_sum(number)

# Виводимо результат
print(result)

   

