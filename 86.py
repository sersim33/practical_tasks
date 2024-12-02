# # Зчитуємо два цілих числа a і b
# a = int(input("Введіть число a (1-1000): "))
# b = int(input("Введіть число b (1-1000): "))

# # Знаходимо максимальне число за допомогою арифметичних операцій
# max_value = (a + b + abs(a - b)) // 2

# # Виводимо результат
# print(max_value)


# Зчитуємо два цілі числа a і b
a = int(input("Введіть число a (1-1000): "))
b = int(input("Введіть число b (1-1000): "))

# Обчислюємо різницю
difference = a - b

# Обчислюємо абсолютну величину різниці
absolute_difference = abs(difference)

# Обчислюємо суму a, b і абсолютної величини різниці
sum_values = a + b + absolute_difference

# Знаходимо максимальне число за допомогою арифметичних операцій
max_value = sum_values // 2

# Виводимо всі значення в одній формулі
print(f"Формула: max_value = ({a} + {b} + |{difference}|) // 2 = ({a} + {b} + {absolute_difference}) // 2 = {max_value}")





    