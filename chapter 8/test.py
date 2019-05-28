import math

def square_root(x):
    """Finds the square root of a single given integer. If the value
    is not a perfect square, the radical is simplified to a mixed
    radical."""
    rad = int(x)
    mods = []
    # if rad >= 0:
    squares = []
    i = 2
    q = int(math.sqrt(rad))
    while i ** 2 <= rad:
        s = i ** 2
        squares.append(s)
        i += 1
    squares.reverse()
    if rad in squares:
        root = f"{q}"
    else:
        for z in squares:
            mod = rad % z
            mods.append(mod)
            if 0 in mods:
                div = int(rad / z)
                print(z)
                print(div)
                sq = int(math.sqrt(z))
                print(sq)
                root = f"{sq}√{div}"
                break
            else:
                root = "1"
                break
    return root
print(square_root(90))
