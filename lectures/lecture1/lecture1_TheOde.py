"""
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().
"""

import numpy as np


def argmax(values):
    """
    Return the index of the maximum value in a collect.

    Paramteres
    -----------
    values
        Sequence of values

    Return
    -----------
    imax : int
        Index of maximum
    """

    N = len(values)

    if N == 0:
        print("Length zero sequences not support")
        return

    imax = -1
    # Set the vmax to the lowest possible value
    vmax = -np.inf

    for i in range(N):
        # First iteration: value = 2
        value = values[i]
        # Check whether this value is larger than any previous
        if value > vmax:
            # Update the index and the vmax
            imax = i
            vmax = value

    return imax


values = [2, 3, -1, 7, 4]
imax = argmax(values)

print(f"The maximum value is located at index {imax}")

# Try a version without values, program will return None
#values = []
#imax = argmax(values)
#print(f"The maximum value is located at index {imax}")


# Compure to NumPy's argmax
j = np.argmax(values)
print(f"The maximum value is located at index {j}")

