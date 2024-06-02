def format_as_percentage(number):
    # Форматування числа як відсотка
    return f"{number:.2%}"

def main():
    # Вхідні дані
    numbers = [0.05, 0.245, 1]
    
    # Обробка кожного числа
    for number in numbers:
        formatted_number = format_as_percentage(number)
        print(f"{number} у форматі відсотків: {formatted_number}")

if __name__ == "__main__":
    main()
