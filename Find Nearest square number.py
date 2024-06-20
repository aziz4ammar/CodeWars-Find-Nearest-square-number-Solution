def nearest_sq(n):
    c=1
    while c**2<n:
        c=c+1
    if abs(n-c**2)<=abs(n-(c-1)**2):
        return c**2
    else :
        return (c-1)**2