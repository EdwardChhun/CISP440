from queue import deque    # For O(1) operations and lookup 

def convert_to_adj_list(file):
    arr = []
    with open(file,"r") as f:
        for line in f:
            arr.append([int(char) for char in line.strip().split()])
            
    return arr
    
# To move to the next adjacent row, i move (row, col+1) and (row+1, col+1)
    
def bfs(triangle):
    maxSum = 0
    root = triangle[0][0]
    
    # Go to next adjacent nodes and add to find max sum
    q = deque([(0,0, root)])
    
    while q:
        row, col, currSum = q.popleft()
        maxSum = max(maxSum, (currSum))
        
        if row < len(triangle) - 1:
            q.append((row + 1, col, currSum + triangle[row+1][col]))  # Append the left child
            q.append((row + 1, col + 1, currSum + triangle[row+1][col+1]))  # Append the right child
        

    return maxSum            
    
    
print(f"test case: {bfs(convert_to_adj_list("9_test.txt"))}")
print(f"answer for given triangle: {bfs(convert_to_adj_list("9.txt"))}")