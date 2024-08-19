
def int_to_bin_with_leading_zeros(number):
    """
    Перетворює ціле число в бінарний формат з провідними нулями.
    
    :param number: Ціле число для перетворення
    :return: Бінарний рядок з провідними нулями
    """
    binary_string = bin(number)[2:]  # Перетворюємо число в бінарний формат без '0b'
    return binary_string.zfill(8)  # Додаємо провідні нулі до 8 бітів

# Вхідні дані
numbers = [389, 65, 2]

# Перетворюємо і виводимо результати
for number in numbers:
    binary_representation = int_to_bin_with_leading_zeros(number)
    print(binary_representation)

