# Number of steps in Euclidean Algorithm

# (x, y) ;  x >= y
# (x, y) => (y, x mod y) until y = 0

# Fibonacci sequence using fib(n+2) and f(n+1) gives us the x, y for n-amount of steps 
# https://en.wikipedia.org/wiki/Euclidean_algorithm#Algorithmic_efficiency

def fib(n) -> list:
    fib = [1, 1]
    for _ in range(2, n + 2):  # Need F(n+2)
        fib.append(fib[-1] + fib[-2])
    return fib
    
    
def foo(x, y, step=0) -> None:
    # Using recursion
    print(f"{x , y}")
    if y != 0:
        foo(y, x % y, step + 1)
    else:
        print(f"steps: {step}")
        

def bar(steps) -> None:
    """ 
    steps : list
    e.g. [1, 3, 4, 2]
    """
    step = max(steps)
    fibList = fib(step + 2)
    
    res = []
    for i in steps:
        x, y = fibList[i + 1], fibList[i] # Indexes of the list of fib sequences
        res.append(f"{x} {y} ")
        
    print("".join(res))    

# Verify possible answers from example
print("Verifying examples")
foo(111, 111)
foo(9, 7)


steps = [7, 16, 29, 40, 41, 57, 70, 71]

bar(steps)
bar([5, 11])

# NOTE
# Hope this output format and input format is okay
# Using bar[list] to print into string without using the second string of numbers as input
    
print("Main program starts here: \n \n \n ")

if __name__ == "__main__":
    first_input = input() # Just to take the input, I don't actually need it
    second_input = input() # This is the list of t integer values of target steps
    
    # Example Input
    # 2
    # 1 3
    steps = list(map(int, second_input.split()))
    
    bar(steps)
    



