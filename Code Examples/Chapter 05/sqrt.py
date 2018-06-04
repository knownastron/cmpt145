def sqrt(x):
    """	
Purpose:
    Approximate the square root of a given number, x.
Pre-conditions:
    x: A non-negative number
Post-conditions:
    (none)
Return:
    a number y such that y*y is close to x.
    Note: if x is negative, the value None is returned
    """
    if x < 0:
        return None
    else:
        y = 1.0
        while abs(x - y*y) > 0.001:
            y = (y + x/y)/2.0
        return y
