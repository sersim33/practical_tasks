# Зчитування двоцифрового числа з клавіатури
number = int(input("Введіть двоцифрове число: "))

if number >=10:
    if number <=99:
        tens = (number // 10) % 10
        print(tens)
    else:
        print("error")

else:
    print("need more")
