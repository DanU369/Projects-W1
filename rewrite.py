def min(x,y):
    if x <= y:
        return x
    elif x > y:
        return y
djkhvlzhjxvLXMvklzxj
xvzkjkzxvklzxjvklxz
zxvmzxkjvnkzxjvkjxz

def max(x,y):
    if x <= y:
        return y
    elif x > y:
        return x


def len(iterable):
    i=0
    for letter in iterable:
        i=i+1
    return i


def multiply(x,y):
    i=1
    xn=x
    while i<y:
        xn=xn+x
        i=i+1
    return xn


def pow(x,y):
    i=1
    xp=x
    while i<y:
        xp=xp*x
        i=i+1
    return xp


def divmod(x,y):
    cat=0
    xd=x
    rest=0
    while xd>y:
        xd=xd-y
        cat=cat+1
        rest=x-(cat*y)
    return cat,rest


