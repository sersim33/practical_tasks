
n = int(input("Введіть число n: "))

# Перетворення числа на рядок і повторення його 100 разів
repeated_number_str = str(n) * 10

# Перетворення повтореного рядка назад у ціле число
repeated_number = int(repeated_number_str)

# Піднесення числа до квадрату
result = repeated_number ** 2

print(repeated_number_str)
print(result)
