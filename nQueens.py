from itertools import permutations
def nQueens(n):
    sol = 0
    for combo in permutations(range(n)):
        if(n == (len(list(set(combo[i] + i for i in combo)))) == (len(list(set(combo[i] - i for i in combo))))):
            sol += 1
            print(combo)
    return sol

print(nQueens(8)) # 8 queens problem as demo here.
