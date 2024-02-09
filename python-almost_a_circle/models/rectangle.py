'''Importing the base file'''
from models.base import Base

'''Creating the class rectangle that inherits from Base'''
class Rectangle(Base):
    '''Creating instance attributes to contain width and height
        Calling the super() function from the Base class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    '''Creating getters and setters for all the created instance'''
    @property
    def width(self):
        '''Retrives the width of the rectangle'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''setter for the widht of the rectangle'''
        '''Raising exceptions if the input is not an integer or input is <= 0'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value


    '''Getter and setter for the height'''
    @property
    def height(self):
        '''Retrives the height of the rectangle'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''setter for the height of the rectangle'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    '''Getter and setter for the x value'''
    @property
    def x(self):
        '''Retrives the x value'''
        return self.__x
    
    @x.setter
    def x(self, value):
        '''setter for the x value'''

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    '''Getter and setter for y value'''
    @property
    def y(self):
        '''Retrives the y value'''
        return self.__y
    
    @y.setter
    def y(self, value):
        '''setter for the y value'''

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    
    '''Creating a method to get the area of the rectangle'''

    def area(self):
        '''This takes the width and multplies by height and returns area'''
        return self.__width * self.__height
    
    def display(self):
        '''Prints in stdout the Rectangle instance with the character #'''
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    '''Overiding the __str__ method'''
    def __str__(self):
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    '''Adding a method that assigns an argument to each attribute'''
    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args is not None and len(args) is not 0:
            list_atrr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrr[i], args[i])
        # if len(args) > 0:
        #     if len(args) >= 1:
        #         self.id = args[0]
        #     if len(args) >= 2:
        #         self.width = args[1]
        #     if len(args) >= 3:
        #         self.height = args[2]
        #     if len(args) >= 4:
        #         self.x = args[3]
        #     if len(args) >= 5:
        #         self.y = args[4]
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)