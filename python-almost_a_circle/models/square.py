""" This module contains the class Square """

from models.rectangle import Rectangle

'''Creating class square'''
class Square(Rectangle):
    '''Class square that has inherited all logic from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Creating new instances for the square and calling the instances from rectangle'''
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)
    
    @property
    def size(self):
        """Property retriever for size.

        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square.
        Args:
            value (int): width of square.
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value