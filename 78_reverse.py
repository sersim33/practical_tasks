
def reverse_number(n):
    # Перетворюємо число в рядок, реверсуємо його, а потім знову перетворюємо в число
    reversed_number = int(str(n)[::-1])
    return reversed_number

# Введення трицифрового числа
n = int(input("Введіть трицифрове число: "))

# Отримання реверсного запису
reversed_n = reverse_number(n)

# Виведення результату
print(f"Реверсний запис: {reversed_n}")
