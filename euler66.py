LIMIT = 100000

# Return largest value of X given by a set numbers "D"
def solver(D) -> int:
    # Check if D is a non squared integer
    if (int(D ** 0.5) ** 2 == D):
        return 0
    
    # finding the smallest value of x that makes y a non-trivial integer solution from the equation
    for x in range (1, LIMIT):
        y_2 = (x**2 - 1) / D
        if y_2>0 and y_2.is_integer():
            y = int(y_2**0.5)
            if y**2 == y_2:
                return x
            
    # prevent's return type -> None
    return 0
            
answer = 0
bar = 0
top = 50

for i in range(1, top + 1):
    res = solver(i)
    print("current count:", i, "result:" , res)
    if (res > answer):
        bar = i
        answer = res
    
print("####")
print(f"For D less than or equal to {top} the largest value of x is {answer} when D is {bar}")
print("####")