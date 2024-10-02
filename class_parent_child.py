class Parent():
    """
    The Parent object is ...

    Args:
        arg (str): The arg is used for...
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
    """

    def __init__(self, hair_color, temper):
        self.hair_color = hair_color
        self.temper = temper

    def sleeping_style(self):
        print('big fan of nap')


class Child(Parent):
    """ 
    The Child object is ...

    Args:
        arg (str): The arg is used for...
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
    """

    def __init__(self, hair_color, temper):
        # call the base class init function
        super().__init__(hair_color, temper)

    def sleeping_style(self):
        # extending the base class method
        super().sleeping_style()
        print('tossing and turning')

"""
if __name__ == '__main__':
    # create instance of the child class
    enow = Child('black', 'slow in anger')
    enow.sleeping_style()
    print(enow.hair_color)
    print(enow.temper)
"""

