# Sources: https://www.youtube.com/watch?v=Qej8V1M1e2A
#          https://en.wikipedia.org/wiki/Josephus_problem#The_general_case

def foo(n, k) -> int:
    
    # Base Case
    if (n==1):
        return 1
    # Recursive case
    # Reduce the amount of person after a person has been killed
    # We sub for the k+1'th position as our initial position after each reccurence
    # Then we find a base case where n == 1, then it would traverse back down the recursive stack
    # The modulo is to take in account for the "circular" structure of the problem
    # So we wouldn't have to implement a circular list structure and make sure the positions doesn't go out of index
    else:
        return (foo(n-1, k) + k-1) % n + 1

# For a base 2 case, I've watched a video from numberphile and 
# You can represent the answer in terms of n = 2^a + l
# Where l is the remaining number and the answer to the josephus problem
# would be 2l + 1

# Or if you reorder the first bit by popping it and appending it to the back of the "binary-list" 
# representation of n-amount of people, you find your answer.

# Source: https://www.youtube.com/watch?v=uCsD3ZGzMgE
# Using a built in integer to binary converter
def num_to_binary_list(num) -> list:
    return [int(n) for n in bin(num)[2:]] # Slices from index 2 because it prints the "0b" 

# Takes in the array of binary representation of n, and then pops the first position
# and append it to the back
def bar(arr) -> int:
    arr.append(arr.pop(0))
    return (int(''.join(map(str, arr)), 2))


# Main
n = [10, 30, 86]
k = [3, 9, 23]
for i in range(3):
    print(f"N = {n[i]} K = {k[i]} Stand at pos #{foo(n[i], k[i])}.")

# Second part
n = 1531502
print(f"N = {n} K = 2 Stand at pos #{bar(num_to_binary_list(n))}")