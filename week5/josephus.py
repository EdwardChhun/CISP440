def foo(n, k):
    
    # Base Case
    if (n==1):
        return 1
    # Recursive case
    # 
    else:
        return (foo(n-1, k) + k-1) % n + 1
    
n = 30
k = 9

print(f"Best place to live is {foo(n, k)}.")