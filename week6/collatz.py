# This is for memoization so for the terms that already computed, no need to compute again
from functools import cache
import time

@cache # cache decorator just to memoize 
def collatz(n: int, counter = 0) -> int:
    print(int(n))
    if n == 1:
        return counter + 1
    
    if n % 2 == 0:
        return collatz(n/2,counter + 1)
    else:
        return collatz(3*n + 1,counter + 1)
    
# Just testing to program
# counter = 0
# n = int(input("Collatz sequence n = "))
# counter = collatz(n)

# print(f"{n} has {counter} terns")

# Question
# What starting number produces the largest amount of sequences under 1 million
# Start from 1M and down to 1, have a counter count the amount of times the procedure has run, 
# and keep check of the max prodcedure?
def max_terms():
    limit = 1000000
    max_length = 0
    starting_num = 0
    for i in range(limit, 0, -1):
        length = collatz(i)
        if length > max_length:
            starting_num = i
            max_length = length
        
    print(f"The max number of terms is {max_length}, with starting number {starting_num}")

# Main driver

if __name__ == "__main__":
    # Example 1 with starting_number 13
    length = collatz(13)
    print("Max terms for 13 is",length)
    time.sleep(5)
    
    
    start_time = time.time()
    
    # Finding max length
    # This ran in around 99 seconds for me
    # I think this is a reasonable time
    max_terms()
    
    end_time = time.time()
    
    print(f"program ran in {end_time - start_time} seconds")
    
    
    
