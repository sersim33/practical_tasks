
#Напишіть програму для друку цілих чисел з нулями ліворуч, якщо введене число має у своєму записі менше 5 розрядів.

# def print_with_zeros(num):
#     # Визначення формату для друку числа з нулями ліворуч
#     format_string = "{:0>5}".format(num)
#     # Виведення числа з нулями ліворуч
#     print(format_string)

# # Приклад використання
# num = int(input("Введіть ціле число: "))
# print_with_zeros(num)


def print_with_zeros(num):
    num_str = str(num).zfill(5)
    print(num_str)

# Приклад використання:
input_num = int(input("Введіть ціле число: "))
print_with_zeros(input_num)

