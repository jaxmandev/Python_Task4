# import the parent class
from phase1 import Basic_features

# initiate child class
class Extra_features(Basic_features):
    def __init__(self):
        super().__init__()
        
        # create a divisible by function that return boolean
        def modulus(self, arg1, arg2):
            if arg1 % arg2 == 0:
                return True
            else:
                return False
        
        # create a function to measure the area of a triangle 
        def triangle_area(self, base, height):
            area = base * height * 0.5
            return area
        
        # create inch to cm converter function 
        def inch_to_cm(self, arg):
            cm = arg * 2.54
            return cm

test = Extra_features()
print(test.inch_to_cm(98))