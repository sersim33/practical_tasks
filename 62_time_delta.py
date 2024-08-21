import datetime

def seconds_to_time(seconds):
    # Використання timedelta для перетворення секунд у дні, години, хвилини та секунди
    time_delta = datetime.timedelta(seconds=seconds)
    
    # Витягування компонентів днів, годин, хвилин та секунд з timedelta
    days = time_delta.days
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

# Введення кількості секунд
total_seconds = int(input("Введіть кількість секунд: "))

# Виклик функції для перетворення
days, hours, minutes, seconds = seconds_to_time(total_seconds)

# Виведення результату
print(f"Дні: {days}")
print(f"Години: {hours}")
print(f"Хвилини: {minutes}")
print(f"Секунди: {seconds}")
