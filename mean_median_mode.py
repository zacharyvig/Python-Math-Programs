"""Fun with descriptive statistics."""


def sort(xs: list[int]) -> list[int]:
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


def mean(xs: list[int]) -> float:
    r: int = 0
    for item in xs:
        r += item
    return r / len(xs)


def median(xs: list[int]) -> float:
    ys: list[int] = sort(xs)
    i: int = len(ys) // 2
    if len(ys) % 2 == 0:
        return (ys[i - 1] + ys[i]) / 2
    else:
        return ys[i]


def unimode(xs: list[int]) -> int:
    r: int = 0
    c: int = 0
    for i in xs:
        d: int = 0
        for j in xs:
            if i == j:
                d += 1
        if d > c:
            c = d
            r = i
    return r


l: int = int(input("int count = "))
i: int = 0
xs: list[int] = []
while i < l:
    xs.append(int(input(f"x{i + 1} = ")))
    i += 1

print(f"mean = {mean(xs)}")
print(f"median = {median(xs)}")
print(f"mode = {unimode(xs)}")