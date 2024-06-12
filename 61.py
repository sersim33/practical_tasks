
def alarm_time(t, h, m):
    
    total_min = t + h * 60 + m 

    # hours, minutes = divmod(t, 60)
    hours = total_min // 60  
    minutes = total_min % 60  
    
    # Враховуємо, що години можуть бути більше 24
    hours = hours % 24
    
    return hours, minutes

# Тестування функції
t = 400
h = 1
m = 40 
hours, minutes = alarm_time(t, h, m)
print(f"{hours}\n{minutes}")


