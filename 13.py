import math

# Зчитування радіуса кола від користувача
radius = float(input("Введіть радіус кола: "))

# Обчислення площі кола
area = math.pi * radius**2

# Обчислення довжини кола
circumference = 2 * math.pi * radius

# Виведення результатів з трьома символами після десяткової крапки
print(f"Площа кола: {area:.3f}")
print(f"Довжина кола: {circumference: .4f}")
