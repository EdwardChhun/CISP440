import heapq

def dijkstra_right_down(grid):
    """
    Allowed moves: right and down.
    Computes minimal path sum from grid[0][0] to grid[-1][-1].
    """
    rows, cols = len(grid), len(grid[0])
    moves = [(0, 1), (1, 0)]  # only right and down

    # Create a matrix for costs and initialize with infinity
    costs = [[float('inf')] * cols for _ in range(rows)]
    costs[0][0] = grid[0][0]

    # Priority queue stores elements as (current_cost, i, j)
    pq = [(grid[0][0], 0, 0)]

    while pq:
        cur_cost, i, j = heapq.heappop(pq)

        # If the cost is outdated, skip this entry
        if cur_cost > costs[i][j]:
            continue

        # If we've reached the destination, return the cost
        if i == rows - 1 and j == cols - 1:
            return cur_cost

        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                new_cost = cur_cost + grid[ni][nj]
                if new_cost < costs[ni][nj]:
                    costs[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))
    
    return costs[rows - 1][cols - 1]


def dijkstra_right_down_up(grid):
    """
    Allowed moves: right, down, and up.
    Computes minimal path sum from grid[0][0] to grid[-1][-1].
    """
    rows, cols = len(grid), len(grid[0])
    moves = [(0, 1), (1, 0), (-1, 0)]  # right, down, and up

    costs = [[float('inf')] * cols for _ in range(rows)]
    costs[0][0] = grid[0][0]

    pq = [(grid[0][0], 0, 0)]

    while pq:
        cur_cost, i, j = heapq.heappop(pq)
        if cur_cost > costs[i][j]:
            continue

        if i == rows - 1 and j == cols - 1:
            return cur_cost

        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                new_cost = cur_cost + grid[ni][nj]
                if new_cost < costs[ni][nj]:
                    costs[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))
    
    return costs[rows - 1][cols - 1]


def dijkstra_four_directions(grid):
    """
    Allowed moves: right, down, up, and left.
    Computes minimal path sum from grid[0][0] to grid[-1][-1].
    """
    rows, cols = len(grid), len(grid[0])
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # right, down, up, left

    costs = [[float('inf')] * cols for _ in range(rows)]
    costs[0][0] = grid[0][0]

    pq = [(grid[0][0], 0, 0)]

    while pq:
        cur_cost, i, j = heapq.heappop(pq)
        if cur_cost > costs[i][j]:
            continue

        if i == rows - 1 and j == cols - 1:
            return cur_cost

        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                new_cost = cur_cost + grid[ni][nj]
                if new_cost < costs[ni][nj]:
                    costs[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))
    
    return costs[rows - 1][cols - 1]


# Provided 5x5 matrix (from 11_test.txt)

def create_2d_array(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            
            if not line:
                continue
            
            row = [int(num.strip()) for num in line.split(",")]
            grid.append(row)
            
    return grid


testGrid = [
    [131, 673, 234, 103,  18],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 696],
    [805, 732, 524,  37, 331]
]

grid = create_2d_array("11.txt")

#Test Case:
print("TEST CASE:")
min_sum_rd = dijkstra_right_down(testGrid)
print("Dijkstra (Right, Down): Minimum Path Sum =", min_sum_rd)

min_sum_rdu = dijkstra_right_down_up(testGrid)
print("Dijkstra (Right, Down, Up): Minimum Path Sum =", min_sum_rdu)

min_sum_four = dijkstra_four_directions(testGrid)
print("Dijkstra (Right, Down, Up, Left): Minimum Path Sum =", min_sum_four)

#Answer:
print("ANSWER: ")
min_sum_rd = dijkstra_right_down(grid)
print("Dijkstra (Right, Down): Minimum Path Sum =", min_sum_rd)

min_sum_rdu = dijkstra_right_down_up(grid)
print("Dijkstra (Right, Down, Up): Minimum Path Sum =", min_sum_rdu)

min_sum_four = dijkstra_four_directions(grid)
print("Dijkstra (Right, Down, Up, Left): Minimum Path Sum =", min_sum_four)
