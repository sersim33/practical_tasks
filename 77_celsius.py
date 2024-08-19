
def convert_temperature(celsius):
    # Перетворення в градуси Фаренгейта
    fahrenheit = 32 + 9/5 * celsius

    # Перетворення в градуси Кельвіна
    kelvin = celsius + 273.15

    return fahrenheit, kelvin

# Введення температури у градусах Цельсія
celsius = float(input("Введіть температуру у градусах Цельсія: "))

# Конвертація
fahrenheit, kelvin = convert_temperature(celsius)

# Виведення результатів
print(f"Температура у градусах Фаренгейта: {fahrenheit:.2f} °F")
print(f"Температура у градусах Кельвіна: {kelvin:.3f} K")

