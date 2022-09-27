class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def __str__(self):
        return f"Rectangle:(width={str(self.width)}, height={str(self.height)})"

    def set_width(self, width):
        self.width=width

    def set_height(self, height):
        self.height=height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self): 
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**0.5)

    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        square=("*"*self.width + "\n")*self.height
        return square

    def get_amount_inside(self, shape): 
        max_width=self.width//shape.width
        max_height=self.height//shape.height
        return max_width*max_height

class Square(Rectangle):
    def __init__(self, lenght):
        self.width=lenght
        self.height=lenght

    def __str__(self):
        return f"Square(side={str(self.width)})"
    
    def set_side(self, lenght):
        self.width = lenght
        self.height = lenght
        
    def set_width(self, lenght):
        self.width = lenght
        self.height = lenght
        
    def set_height(self, new_lenght):
        self.width = new_lenght
        self.height = new_lenght
