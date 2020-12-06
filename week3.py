import math
import cmath
from week1 import cartesian_to_polar as cf

print(cf(-15,-8))
print(cf(math.sqrt(1/3),math.sqrt(2/3)))

#multiplying complex numbers

def cmultiply(a,b):
    return a*b
print(cmultiply(2-7j,3-2j))

#magnitude of complex numbers

print(abs(complex(5,-12)))

#converting complex numbers to polar form
def cm2polar(a):
    """
    converts the complex number into polar form,returns a tuple r,phi where r is 
    modulus, phi is phase angle
    """
    return cmath.polar(a)

def polar_display(a,b):
    """
    displaying the polar form of complex number a+ib in conventional form
    """
    q=math.pi/b
    return f"{a}e**iPI/{q}"

r,phi=cm2polar(complex(0,5))
print(polar_display(r,phi))