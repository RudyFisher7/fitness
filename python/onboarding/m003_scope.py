from enum import Enum

my_global_x = 1 # in global scope, can access throughout this module
my_x = 2

def my_function():
    my_local_x = 0
    my_x = 3
    print(my_x)


my_function() # prints 3
print(my_x) # prints 2


def my_outer_function():
    outer_message = "hello outer world" # this is in a scope that encloses the inner function
    def my_inner_function():
        nonlocal outer_message # this must be before any usage of this variable
        print(outer_message)
        outer_message += " and all of humanity!"
    
    my_inner_function() # prints the outer message
    return my_inner_function

my_functor = my_outer_function() # prints the outer message

my_functor() # does the concatenated string

my_functor_2 = my_outer_function() # this starts over with the original outer message

my_functor() # this contatenates a second time
my_functor_2() # this only has 1 concatenation, like my_functor before


class Ship:
    is_buoyant = True # class scope

    def __init__(self, in_name: str):
        self.name = in_name
    
    def get_name(self) -> str:
        return self.name # instance scope (can access self keywork)

class SmallShip(Ship): # this class has access to all its super's stuff, but not vice versa
    class Size(Enum):
        SMALL = 0
        MEDIUM = 1
        LARGE = 2

    def __init__(self, in_name: str, in_size: Size):
        super().__init__(in_name)

        self.size = in_size