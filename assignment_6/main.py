import numpy as np
from matplotlib import pyplot as plt

def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {o}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

x = np.linspace(0, 9, 10)
coeffs = [-3, -3, -2]
plt.plot(x, PolyCoefficients(x, coeffs))
plt.show()


#####
# Constructing polynomial
# p1 = np.poly1d([1, 2])
# p2 = np.poly1d([4, 9, 5, 4])

# print ("P1 : ", p1)
# print ("\n p2 : \n", p2)

# # Solve for x = 2
# print ("\n\np1 at x = 2 : ", p1(2))
# print ("p2 at x = 2 : ", p2(2))

# # Finding Roots
# print ("\n\nRoots of P1 : ", p1.r)
# print ("Roots of P2 : ", p2.r)

# # Finding Coefficients
# print ("\n\nCoefficients of P1 : ", p1.c)
# print ("Coefficients of P2 : ", p2.coeffs)

# Finding Order
# print ("\n\nOrder / Degree of P1 : ", p1.o)
# print ("Order / Degree of P2 : ", p2.order)