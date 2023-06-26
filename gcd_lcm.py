"""Fun with math functions."""


def gcd(x: int, y: int) -> int: # greatest common divisor
    a: int = max(x, y)
    b: int = min(x, y)
    
    while a % b != 0:
        r: int = a % b
        a = b
        b = r

    return f"gcd = {b}"


def lcm(x: int, y: int) -> int: # least common multiple
    a: int = max(x, y)
    b: int = min(x, y)
    c: int = a

    while c % b != 0:
        c += a
    
    return f"lcm = {c}"
    

x: int = int(input("x = "))
y: int = int(input("y = "))

print(gcd(x, y))
print(lcm(x, y))