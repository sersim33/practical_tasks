
def calculate(students):
    # Обчислюємо кількість парт для одного класу
    result = (students + 1) // 2
    return result

# Введення кількості учнів у трьох класах
a = int(input("add number of students in class A: "))
b = int(input("add number of students in class B: "))
c = int(input("add number of students in class C: "))

# Обчислення кількості парт для кожного класу і сума
desks = calculate(a) + calculate(b) + calculate(c)

# Виведення результату
print(f'Need {desks} desks')
