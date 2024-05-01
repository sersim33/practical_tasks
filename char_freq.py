from collections import Counter

# Введення рядка від користувача
input_string = input("Введіть рядок: ")

# Підрахунок символьної частоти з використанням Counter
char_freq = Counter(input_string)

print(char_freq)
