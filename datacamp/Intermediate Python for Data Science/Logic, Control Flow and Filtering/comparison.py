
"""Boolean operators with Numpy
Before, the operational operators like < and >= worked with Numpy arrays out of the box.
Unfortunately, this is not true for the boolean operators and, or, and not.

To use these operators with Numpy, you will need 
		np.logical_and()
		np.logical_or()
		np.logical_not(). 
Here's an example on the my_house and your_house arrays from before to give you an idea:

np.logical_and(your_house > 13, 
               your_house < 15)

"""

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11,your_house < 11))