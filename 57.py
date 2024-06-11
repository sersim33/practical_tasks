def calculate_flour_mass(pie_mass):
    """
    Функція для обчислення маси борошна в пирозі.
    
    :param pie_mass: Загальна маса пирога в кг.
    :return: Маса борошна в пирозі в грамах.
    """
    # Масова частка яблук (60%) та тіста (40%)
    dough_mass = pie_mass * 0.40
    
    # Масова частка борошна в тісті (70% від тіста)
    flour_mass = dough_mass * 0.70
    
    # Перетворюємо масу борошна з кг на грами
    flour_mass_grams = flour_mass * 1000
    
    return flour_mass_grams

# Запитуємо користувача ввести масу пирога в кг
pie_mass = float(input("Введіть масу пирога в кг: "))

# Викликаємо функцію і отримуємо результат
flour_mass_grams = calculate_flour_mass(pie_mass)

# Виводимо результат
print(f"Маса борошна в пирозі: {flour_mass_grams:.2f} грамів")
