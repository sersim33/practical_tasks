class Shape:
    width = 5
    height = 5
    printChar = '#'

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")

    def print(self):
        for i in range(self.height):
            self.printRow(i)

# class Square(Shape):
#     def printRow(self, i):
#         print(self.printChar * self.width)

class Triangle(Shape):
    def printRow(self, i):
        num_chars = 2 * i + 1
        num_spaces = (self.width * 2 - 1 - num_chars) // 2
        print(' ' * num_spaces + self.printChar * num_chars + ' ' * num_spaces)

# # Приклад використання:
# print("Square:")
# square = Square()
# square.print()

print("\nTriangle:")
triangle = Triangle()
triangle.print()
