
from datetime import timedelta

def convert_to_seconds(days, hours, minutes, seconds):
    total_seconds = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds).total_seconds()
    return total_seconds



def main ():
    try:
        days = int(input("add days: "))
        hours = int(input("add hours: "))
        minutes = int(input("add min: "))
        seconds = int(input("add sec: "))

    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return
    
    total_seconds = convert_to_seconds(days, hours, minutes, seconds)
    print(f"Загальна кількість секунд: {total_seconds}")

if __name__ == "__main__":
    main()