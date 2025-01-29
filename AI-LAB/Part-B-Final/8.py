# 8.FOPL

from sympy import symbols, Not

def resolve(c1, c2):
    return next((list(set(c1 + c2) - {l1, l2}) for l1 in c1 for l2 in c2 if l1 == Not(l2) or l2 == Not(l1)), [])

def resolution(clauses):
    new = list(clauses)
    steps = []
    while True:
        n = len(new)
        pairs = ((new[i], new[j]) for i in range(n) for j in range(i+1, n))
        for c1, c2 in pairs:
            res = resolve(c1, c2)
            if not res: 
                steps.append(f"Empty clause derived from {c1} and {c2}")
                return True, steps
            if res not in new: 
                new.append(res)
                steps.append(f"New clause {res} derived from {c1} and {c2}")
        if len(new) == n: return False, steps

if __name__ == "__main__":
    P, Q = symbols('P Q')
    clauses = [[P, Not(Q)], [Not(P), Q], [Not(P), Not(Q)]]
    result, steps = resolution(clauses)
    print("Initial clauses:", clauses)
    for step in steps:
        print(step)
    print("Conclusion: The set of clauses is", "unsatisfiable" if result else "satisfiable")