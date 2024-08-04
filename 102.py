
def main():
    # Наперед визначений пароль
    predefined_password = "securepassword"

    # Запитуємо користувача ввести пароль
    user_input = input("Please enter your password: ")

    # Перевіряємо, чи введений пароль співпадає з наперед визначеним паролем
    if user_input == predefined_password:
        print("Password accepted.")
    else:
        print("Sorry, that is the wrong password.")

# Запускаємо основну функцію
if __name__ == "__main__":
    main()
