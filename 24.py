def format_as_percentage(number):
    # Format the number as a percentage
    return f"{number:.0%}"

def main():
    numbers = input("Add numbers separated by spaces: ").split()
    
    # Process each number
    for number in numbers:
        try:
            number = float(number)
            formatted_number = format_as_percentage(number)
            print(f"{number} in percentage format: {formatted_number}")
        except ValueError:
            print(f"{number} is not a valid number")

if __name__ == "__main__":
    main()

