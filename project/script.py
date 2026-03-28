"""
EVERYTHING IS A SCRIPT UNTIL YOU IMPORT IT, 
THEN IT'S A MODULE.
"""

"""
importing area
"""

# import utils

# import utils.math_utils
from utils import math_utils
    # These two are interchangeable

from utils.math_utils import PI 

"""definition area: function/methods, variables
"""

def fun():
    pass

def fun2():
    pass

"""calling area - for main script
"""
if __name__ == "__main__": 
    print("Entering main script.")
    print(PI)
    print(f"this is {__name__}")
    fun()
    fun2()
    print(math_utils.add(2, 2))
    print(math_utils.multiply(3, 2))
