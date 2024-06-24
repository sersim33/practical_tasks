# Отримуємо введену цифру від користувача
try:
    input_value = int(input("Enter a digit (0 or 1): "))
    if input_value in [0, 1]:
        # Використовуємо операцію XOR для обернення значення
        output_value = 1 ^ input_value
        # Виводимо результат
        print(output_value)
    else:
        print("error")
except ValueError:
    print("err")

