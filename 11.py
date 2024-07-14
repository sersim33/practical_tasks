# Зчитування двоцифрового числа з клавіатури
number = int(input("Введіть двоцифрове число: "))

if 10 <= number <= 99:
    tens = number //10
    print(tens)
else:
    print("error")

