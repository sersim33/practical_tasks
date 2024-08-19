
def format_duration(days):
    # Обчислюємо тривалість у годинах, хвилинах і секундах
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    # Виводимо результати з вирівнюванням за лівим краєм у полі шириною 10 знаків
    print(f"{hours:<10} hours")
    print(f"{minutes:<10} minutes")
    print(f"{seconds:<10} seconds")

# Вхідні дані
days = 10

# Виведення результатів
format_duration(days)
