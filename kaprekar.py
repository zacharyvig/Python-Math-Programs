"""Kaprekar's constant (c = 6174)."""

def sortup(xs: list[int]) -> list[int]:
    ys = xs.copy()
    zs: list[int] = []
    while len(ys) > 0:
        a: int = ys[0]
        i: int = 0
        j: int = 0
        while i < len(ys):
            if ys[i] < a:
                a = ys[i]
                j = i
            i += 1
        zs.append(a)
        ys.pop(j)
    return zs

def sortdown(xs: list[int]) -> list[int]:
    ys = xs.copy()
    zs: list[int] = []
    while len(ys) > 0:
        a: int = ys[0]
        i: int = 0
        j: int = 0
        while i < len(ys):
            if ys[i] > a:
                a = ys[i]
                j = i
            i += 1
        zs.append(a)
        ys.pop(j)
    return zs

def intsortup(x: int) -> int:
    xs: list[int] = []
    for i in str(x):
       xs.append(int(i))
    xs = sortup(xs)
    ystr: str = ""
    for i in xs:
        ystr += str(i)
    return int(ystr)

def intsortdown(x: int, c: int) -> int: # for c digits
    xs: list[int] = []
    for i in str(x):
       xs.append(int(i))
    xs = sortdown(xs)
    ystr: str = ""
    for i in xs:
        ystr += str(i)
    while len(ystr) < c:
        ystr += "0"
    return int(ystr)

def eqstr(x: int) -> bool:
    xstr: str = str(x)
    a: str = xstr[0]
    for i in xstr:
        if i != a:
            return False
    return True


def kaprekar(x: int) -> None:
    if len(str(x)) > 4:
        kaprekar(int(input("Must be a four digit number: ")))
    elif len(str(x)) == 4 and eqstr(x):
        kaprekar(int(input("Must have at least one unique digit: ")))
    else:
        print(f"\nYour number: {x :04d} \n")
        s: int = 1
        y0 = x
        y1 = intsortdown(x, 4)
        y2 = intsortup(x)
        while y0 != 6174:
            print(f"({s}) {y0 :04d}")
            print(f"    {y1 :04d} - {y2 :04d} = {y1 - y2 :04d} \n")
            s += 1
            y0 = y1 - y2
            y1 = intsortdown(y0, 4)
            y2 = intsortup(y0)
        else:
            print(f"You've arrived at Kaprekar's Constant in {s - 1} iterations!")


num: int = int(input("Input a four digit number: "))
kaprekar(num)