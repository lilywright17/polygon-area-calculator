class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    
  def set_width(self, width_input):
    self.width = width_input
    
  def set_height(self, height_input):
    self.height = height_input
     
  def get_area(self): 
    area = self.width * self.height
    return area
    
  def get_perimeter(self): 
    perimeter = (2 * self.width) + (2 * self.height)
    return perimeter
    
  def get_diagonal(self): 
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal
  
  def get_picture(self): 
    picture = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      for i in range(self.height):
        line = "*"*self.width + "\n"
        picture += line
    return picture
    pass
    
  def get_amount_inside(self, shape): 
    area = self.get_area()
    shape_area = shape.get_area()
    amount = area/shape_area
    return int(amount)

class Square(Rectangle):
  def __init__(self, input_side):
    self.width = input_side
    self.height = input_side

  def set_side(self, input_side):
    self.set_width(input_side)
    self.set_height(input_side)
    
  def __str__(self):
    return f"Square(side={self.width})"
