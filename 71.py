
def midpoint(x1, y1, x2, y2):
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2
    return x_mid, y_mid


# Вхідні дані
x1, y1 = 3, 5
x2, y2 = 10, -4

# Виклик функції для обчислення середини відрізка
mid_x, mid_y = midpoint(x1, y1, x2, y2)

# Виведення результату
print(f"Координати середини відрізка: ({mid_x}, {mid_y})")

