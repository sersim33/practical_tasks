def count_letters_digits(input_string):
    letters = sum(1 for char in input_string if char.isdigit())
    digits =  sum(1 for char in input_string if char.isalpha())
    return letters, digits

input_string = input("Введіть рядок символів: ")
letters, digits = count_letters_digits(input_string)

print("LETTERS", letters)
print("DIGITS", digits)