#answers to questions 12 13 15 16
#Plancks constant 6.63 * 1 * 10 ^ -34
h=6.63*1e-34

def compute_wavelength(denominator):
    """
    Input is a list consisting of either mass and velocity as first two elements
    or just momentum as the first and only element

    """
    if len(denominator)==1:
        p=denominator[0]
    else:
        p=denominator[0]*denominator[1]
    l=h/p
    return l

def compute_momentum(wavelength):
    return h/wavelength   

if __name__=="__main__":
    print("12)",compute_wavelength([2.5]))
    print("13)",compute_wavelength([5.4*1e-25]))
    print("15)",compute_momentum(6.5*1e-7))
    print("16)",compute_momentum(6*1e-2))

