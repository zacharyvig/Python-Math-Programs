"""Algorithm for Calculating Square Root"""

def sqrt(x: float, eps = .000000000001, roundto = 5) -> float:
    
    guess: float = x / 2
    bound: float = x / guess

    while abs(guess - bound) > eps:
        guess = (guess + bound) / 2
        bound = x / guess

    if round(guess, roundto) == int(guess):
        return(int(guess))
    else:
        return(round(guess, roundto))


x: float = float(input("x = "))
print(sqrt(x))