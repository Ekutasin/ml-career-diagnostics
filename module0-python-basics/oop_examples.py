class Rectangle:
    def __init__(self, width: float, height: float):
        """
        width, height — длины сторон прямоугольника.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Площадь прямоугольника."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Периметр прямоугольника."""
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    rect = Rectangle(3, 5)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())