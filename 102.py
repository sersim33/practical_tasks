
# def main():
#     # Наперед визначений пароль
#     predefined_password = "securepassword"

#     # Запитуємо користувача ввести пароль
#     user_input = input("Please enter your password: ")

#     # Перевіряємо, чи введений пароль співпадає з наперед визначеним паролем
#     if user_input == predefined_password:
#         print("Password accepted.")
#     else:
#         print("Sorry, that is the wrong password.")

# # Запускаємо основну функцію
# if __name__ == "__main__":
#     main()

import datetime

def get_weekday(date_string):
    # Перетворення рядка на об'єкт datetime
    date = datetime.datetime.strptime(date_string, "%d.%m.%Y")
    # Визначення дня тижня
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = days[date.weekday()]
    return weekday

def main():
    date_string = input("Введіть дату народження (дд.мм.рррр): ")
    
    try:
        weekday = get_weekday(date_string)
        print(f"День народження припадає на: {weekday}")
    except ValueError:
        print("Неправильний формат дати. Будь ласка, введіть дату у форматі дд.мм.рррр.")

if __name__ == "__main__":
    main()

