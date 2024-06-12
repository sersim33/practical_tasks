def alarm_time(t):
    # Розділяємо хвилини на години і хвилини

    hours, minutes = divmod(t, 60)
    # hours = t // 60
    # minutes = t % 60
    
    # Враховуємо, що години можуть бути більше 24
    hours = hours % 24
    
    return hours, minutes

# Тестування функції
t = 400  # Наприклад
hours, minutes = alarm_time(t)
print(f"{hours}\n{minutes}")
