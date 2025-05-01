# Boolean operation functions
def Implication(a, b):
    return (not a) or b

def Bicondition(a, b):
    return (a and b) or (not a and not b)

def And(a, b):
    return a and b

def Or(a, b):
    return a or b

def Xor(a, b):
    return (a or b) and not (a and b)

def Not(a):
    return not a

# ========
# PART ONE
# ========

equiv_a = all(
    Or(p, q) == Not(And(Not(p), Not(q)))
    for p in [False, True] for q in [False, True]
)
print("a. These expressions are equivalent" if equiv_a else "a. These expressions are NOT equivalent")

equiv_b = all(
    And(p, Implication(q, r)) == Xor(And(p, q), r)
    for p in [False, True] for q in [False, True] for r in [False, True]
)
print("b. These expressions are equivalent" if equiv_b else "b. These expressions are NOT equivalent")

# Part 2: argument checker
def check_argument(premises, conclusion):
    for p in [False, True]:
        for q in [False, True]:
            for r in [False, True]:
                for s in [False, True]:
                    if all(prem(p, q, r, s) for prem in premises) and not conclusion(p, q, r, s):
                        return False
    return True

# ========
# PART TWO
# ========

# Argument 3
def arg3_prem1(p, q, r, s):
    return Or(p, q)
def arg3_prem2(p, q, r, s):
    return Implication(p, r)
def arg3_concl(p, q, r, s):
    return And(p, Not(p))
arg3_premises = [arg3_prem1, arg3_prem2]
arg3_conclusion = arg3_concl

# Argument 4
def arg4_prem1(p, q, r, s):
    return And(Implication(p, q), Implication(r, s))
def arg4_prem2(p, q, r, s):
    return p
def arg4_concl(p, q, r, s):
    return q
arg4_premises = [arg4_prem1, arg4_prem2]
arg4_conclusion = arg4_concl

# Argument 5
def arg5_prem1(p, q, r, s):
    return Or(p, r)
def arg5_prem2(p, q, r, s):
    return Bicondition(p, q)
def arg5_concl(p, q, r, s):
    return q
arg5_premises = [arg5_prem1, arg5_prem2]
arg5_conclusion = arg5_concl

# Argument 6
def arg6_prem1(p, q, r, s):
    return Or(p, q)
def arg6_concl(p, q, r, s):
    return p
arg6_premises = [arg6_prem1]
arg6_conclusion = arg6_concl

# Argument 7
def arg7_prem1(p, q, r, s):
    return Xor(p, q)
def arg7_prem2(p, q, r, s):
    return Bicondition(q, r)
def arg7_concl(p, q, r, s):
    return r
arg7_premises = [arg7_prem1, arg7_prem2]
arg7_conclusion = arg7_concl

# Argument 8
def arg8_prem1(p, q, r, s):
    return And(p, r)
def arg8_prem2(p, q, r, s):
    return Implication(p, q)
def arg8_concl(p, q, r, s):
    return Bicondition(q, Or(r, p))
arg8_premises = [arg8_prem1, arg8_prem2]
arg8_conclusion = arg8_concl

# Run and print results
arguments = [
    ("Argument 3", arg3_premises, arg3_conclusion),
    ("Argument 4", arg4_premises, arg4_conclusion),
    ("Argument 5", arg5_premises, arg5_conclusion),
    ("Argument 6", arg6_premises, arg6_conclusion),
    ("Argument 7", arg7_premises, arg7_conclusion),
    ("Argument 8", arg8_premises, arg8_conclusion),
]

for name, premises, conclusion in arguments:
    print(f"{name}: Your argument is", "valid." if check_argument(premises, conclusion) else "invalid.")
