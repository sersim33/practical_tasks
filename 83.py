# def seconds_to_time(*args, **kwargs):
#     # Використання args для перших трьох параметрів
#     h1, m1, n1 = args

#     # Використання kwargs для других трьох параметрів
#     h2 = kwargs.get('h2', 0)
#     m2 = kwargs.get('m2', 0)
#     n2 = kwargs.get('n2', 0)
    
#     # Перетворення першого часу в секунди
#     total_seconds1 = h1 * 3600 + m1 * 60 + n1
    
#     # Перетворення другого часу в секунди
#     total_seconds2 = h2 * 3600 + m2 * 60 + n2

#     # Обчислення різниці в секундах
#     output = total_seconds2 - total_seconds1

#     # Виведення результату
#     print(f"Різниця в секундах: {output}")

# # Приклад виклику функції
# seconds_to_time(1, 1, 1, h2=2, m2=2, n2=2)


def time_to_seconds(hours, minutes, seconds):
    """Convert hours, minutes, and seconds to total seconds."""
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_time(*args, **kwargs):
    """Calculate the difference in seconds between two times."""
    # First time point (h1, m1, n1)
    total_seconds1 = time_to_seconds(*args)

    # Second time point (h2, m2, n2)
    total_seconds2 = time_to_seconds(
        kwargs.get('h2', 0),
        kwargs.get('m2', 0),
        kwargs.get('n2', 0)
    )

    # Calculate the difference in seconds
    output = total_seconds2 - total_seconds1

    # Print the result
    print(f"Difference in seconds: {output}")

# Example usage
seconds_to_time(1, 1, 1, h2=2, m2=2, n2=2)
