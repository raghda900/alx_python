"""importing The Base Class From base File"""
from models.base import Base

"""Define the Rectangle class"""
class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates instance object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def __str__(self):
        """STR method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"#
    

    @property