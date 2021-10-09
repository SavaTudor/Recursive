def nextPrim(n):
    """
    returns the lowest prime number greater than n
    """
    next_prim = n
    if next_prim == 0 or next_prim == 1:
        return 2
    if next_prim == 2:
        return 3
    ok = 0
    while not ok:
        next_prim += 1
        if (estePrim(next_prim)):
            return next_prim


def maxPrim(numar):
    """
    returns the greatest prime number which is lower than numar
    """
    if numar == 3:
        return 2
    ok = 1
    while ok:
        ok = 0
        for i in range(2, numar):
            if numar % i == 0:
                ok = 1
        if not ok:
            return numar
        numar -= 1


def sumaLista(l):
    """
    returns the sum of the elements in l
    """
    s = 0
    if len(l) == 0:
        return 0
    for i in range(len(l)):
        s = s + l[i]
    return s


def estePrim(x):
    """
    returns True if x is a prime number, False otherwise
    """
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def nuEste1(x):
    """
    returns true if x equals 1, false otherwise
    """
    if x == 1:
        return False
    else:
        return True


def esteCrescator(lista):
    """
    returns true if lista is sorted ascending, false otherwise
    """
    for i in range(0, len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def validare(n):
    """
    validates the entry parameters
    """
    try:
        if int(n) <= 1 and n != 0:
            return False
    except ValueError:
        return False
    return True
