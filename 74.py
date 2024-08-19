import math

def compute_root_of_repeated_number(n):
    # Крок 2: Підносимо число до 10 степеня
    n_power_10 = n ** 10

    # Крок 3: Записуємо результат чотири рази поспіль
    repeated_number_str = str(n_power_10) * 4

    # Крок 4: Перетворюємо рядок у число
    repeated_number = int(repeated_number_str)

    # Обчислюємо корінь 10-го степеня
    root_10 = repeated_number ** (1/10)

    return root_10

# Вхідні дані
inputs = [181, 3, 45]

# Обробка кожного зразка
for n in inputs:
    result = compute_root_of_repeated_number(n)
    print(f"Result for n={n}: {result}")

