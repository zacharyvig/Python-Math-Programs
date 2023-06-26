"""Digits (c) NY Times, recreated by Zach Vig"""

import random

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

def norepeats(xs: list[int]) -> list[int]:
    ys = xs.copy()
    zs: list[int] = []
    for i in ys:
        if i not in zs:
            zs.append(i)
        else:
            zs.append(i + 1)
    return zs

def genoper(a: int, b: int, diff: str) -> str:
    if diff == "One":
        operators = ['+', '-', '*']
    else:
        operators = ['+', '-', '/', '*']
    operation = str(a) + operators[random.randint(0,len(operators)-1)] + str(b)
    ans = eval(operation)
    while ans < 0 or ans > 500 or not float(ans).is_integer():
        operation = str(a) + operators[random.randint(0,len(operators)-1)] + str(b)
        ans = eval(operation)
    return operation

def main():
    print("Welcome to Digits (c) NY Times, recreated by Zach Vig.")
    
    difficulty = input("At what level of difficulty would you like to play? (One, Two, or Three): ")
    
    while difficulty != "One" and difficulty != "Two" and difficulty != "Three":
        difficulty = input("At what level of difficulty would you like to play? (One, Two, or Three): ")
    
    if difficulty == "One":
        low = 1
        mid = 5
        hi = 10
    elif difficulty == "Two":
        low = 2
        mid = 10
        hi = 20
    else:
        low = 3
        mid = 15
        hi = 25

    r_intarray0 = norepeats(sortup([random.randint(low, mid), 
                                random.randint(low, mid), 
                                random.randint(low, mid), 
                                random.randint(low, mid), 
                                random.randint(mid, hi),
                                random.randint(mid, hi)]))

    accept = False

    while not accept:
        operations = list()
        r_intarray = r_intarray0.copy()

        while len(r_intarray) > 1:
            length = len(r_intarray)
            r_indices = random.sample(range(len(r_intarray)), 2)
            a = r_intarray[r_indices[0]]
            b = r_intarray[r_indices[1]]
            operation = genoper(a, b, difficulty)
            answer = eval(operation)
            operations.append(f"{operation}={int(answer)}")
            r_intarray.remove(a)
            r_intarray.remove(b)
            r_intarray.append(int(answer))

        if r_intarray[0] < 500:
            accept = True

    objective = int(r_intarray[0])
    solution = operations

    print(f"Your random number array is {r_intarray0}.")

    print(f"Your objective value is {objective}.")

    show_sol = input("Good luck! If you'd like to see a possible solution, type 'Show': ")

    if show_sol == "Show":
        print(solution)
    else:
        while show_sol != "Show":
            show_sol = input("If you'd like to see the solution, type 'Show': ")
        print(solution)

if __name__ == "__main__":
    main()