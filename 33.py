# def climbStairs(n: int) -> int:
#     if (n==1 or n==2):
#         return n
#     memo = [0] * (n+1)
#     memo[1] = 1
#     memo[2] = 2
#     for i in range(3,n+1):
#         memo[i] = memo[i-1] + memo[i-2]
#     return memo[-1]

# print(climbStairs(9))


def arithmetic_operations(a, b):
    # Додавання
    addition = a + b
    # Віднімання
    subtraction = a - b
    # Множення
    multiplication = a * b
    # Ділення (перевірка на нульовий дільник)
    division = a / b if b != 0 else 'Division by zero is not allowed'
    # Піднесення до степеня
    exponentiation = a ** b

    # Виведення результатів
    print(f"{a} + {b} = {addition}")
    print(f"{a} - {b} = {subtraction}")
    print(f"{a} * {b} = {multiplication}")
    print(f"{a} / {b} = {division}")
    print(f"{a} ** {b} = {exponentiation}")

# Вхідні дані
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Виклик функції
arithmetic_operations(a, b)
