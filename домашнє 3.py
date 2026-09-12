class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def calculate_area(self) -> int:
        return self.width * self.height

    def calculate_perimeter(self) -> int:
        return 2 * (self.width + self.height)


rect = Rectangle(7, 13)
print(f"Площа: {rect.calculate_area()}")
print(f"Периметр: {rect.calculate_perimeter()}")