# Internal representation
# For the literals just signed/unsigned integers
# For the Clauses can just be a set of literals
# For the Forumals can just be a lists of sets/Clauses

# So the internal representation would be List[Set[int]]

import random
from typing import List, Set, Tuple


def read_input(fileName: str) -> Tuple[List[Set[int]], int]:
    """
    Read a CNF formula from file. Returns a list of clauses (each clause is a set of signed ints)
    and maxNum, the highest variable index.
    Skips empty lines so blank clauses do not introduce unsatisfiability.
    """
    with open(fileName, 'r') as f:
        clause_strs = f.read().splitlines()
    clauses: List[Set[int]] = []
    maxNum = 0
    for s in clause_strs:
        # skip blank lines, on text5 there is a blank line
        if not s.strip():
            continue
        literals = s.split()
        clause: Set[int] = set()
        for lit in literals:
            sign = -1 if lit.startswith('-') else 1
            var = int(lit.lstrip('+-'))
            clause.add(sign * var)
            if var > maxNum:
                maxNum = var
        clauses.append(clause)
    return clauses, maxNum


def generateBoolean(maxNum: int) -> List[bool]:
    """
    Generate a random assignment for variables 1..maxNum.
    Returns a list of booleans of length maxNum.
    """
    return [random.choice([True, False]) for _ in range(maxNum)]


def cnfChecker(clauses: List[Set[int]], assignment: List[bool]) -> bool:
    """
    Check if the given assignment satisfies all clauses in the CNF.
    """
    for clause in clauses:
        satisfied = False
        for lit in clause:
            idx = abs(lit) - 1
            val = assignment[idx]
            if lit < 0:
                val = not val
            if val:
                satisfied = True
                break
        if not satisfied:
            return False
    return True


def monteCarlo(clauses: List[Set[int]], maxNum: int, maxTries: int = 1000000) -> Tuple[bool, List[bool]]:
    """
    Perform up to maxTries random assignments. Return (True, assignment) on success,
    or (False, []) if no satisfying assignment found.
    """
    for _ in range(maxTries):
        assignment = generateBoolean(maxNum)
        if cnfChecker(clauses, assignment):
            return True, assignment
    return False, []


def print_result(filename: str, sat: bool, assignment: List[bool]) -> None:
    """
    Print output in the required format.
    """
    if sat:
        out = ', '.join(f"{i+1}={int(assignment[i])}" for i in range(len(assignment)))
        print(f"{filename} satisfied {out}")
    else:
        print(f"{filename} unsatisfied")


def main():
    files = [
        "test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt",
        "gates1.txt", "gates2.txt", "seats.txt", "virus.txt", "favorites.txt"
    ]
    for fname in files:
        clauses, maxNum = read_input(fname)
        sat, assignment = monteCarlo(clauses, maxNum)
        print_result(fname, sat, assignment)


if __name__ == "__main__":
    main()
