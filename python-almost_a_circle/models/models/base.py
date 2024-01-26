""" This module contains the class Base """

class Base:
    """ defines class Base with private attribute __nb_objects """
    __nb_objects = 0
    
    
    def __init__(self, id=None):
        """
        initializes an instance of class Base 
        
        Variables"
        __nb_objects = 0
        
        Args:
        id = None
        """
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
                