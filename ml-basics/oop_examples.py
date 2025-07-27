class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


#Применение

rect = Rectangle(3, 5)
print("Area:", rect.area(), "Perimetr:", rect.perimeter())