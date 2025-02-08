class Shape:
    def __init__(self):
        self.area_value = 0  

    def area(self):
        print(f"Area of Shape: {self.area_value}")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width  
        print(f"Area of Rectangle with length {self.length} and width {self.width}: {rectangle_area}")


shape = Shape()
shape.area()  

rectangle = Rectangle(5, 3)
rectangle.area()  
