# Binary Boarding
# Partitioning
# Rows 128 numbered 0 - 127
# myColumns 8 numbered 0 - 7
# The last 7 characters or the 5th Character represents front/back
# Should start with the number, which col, and which row in order

# Unique ID -----
# first divide the row by 256, then add 1. Then subtract 3 from the
# myColumn and then multiply what you got from the row by 2 to that power, finally if it is first class
# multiply your result by negative one. In this example, the seat has ID (44/256+1)*(2^(5-3))*-1
# = -4.6875.

# Thought process ----
# I'd wanna break this into 3 parts
# class, myColumn, row. Output like this
# 0RRRBFFFBBF: row 70, myColumn 7, coach, seat ID 20.375.

# Part 1: Either by hand or with code, verify each of the given seat IDs (a, b, and c above) and then
# calculate the seat ID for your boarding pass 0RLRBFBFFFF (8 points).

def top_range(myRange) -> range:
    """Returns the upper half of the given range."""
    mid = (myRange.start + myRange.stop) // 2 
    return range(mid, myRange.stop)

def bot_range(myRange) -> range:
    """Returns the lower half of the given range."""
    mid = (myRange.start + myRange.stop) // 2 
    return range(myRange.start, mid)
    
def solver(boardingPass) -> int:
    
    # Seat class condition
    seatClass = "first class" if boardingPass[0] == "1" else "coach"
    
    # Find myColumn
    colRange = range(0, 8)
    col = boardingPass[1:4]
    myColumn = 0

    for i in col:
        colRange = top_range(colRange) if i == "R" else bot_range(colRange)
            
    myColumn = colRange.start
    
    # Find Row (I could refactor since it is similar but nahhhhhh)
    row = boardingPass[4:]
    
    rowRange = range(0, 128)
    myRow = 0
    for i in row:
        rowRange = top_range(rowRange) if i == "B" else bot_range(rowRange)
            
    myRow = rowRange.start
    
    seatID = ((myRow / 256) + 1) * (2 ** (myColumn - 3)) 
    if seatClass == "first class":
        seatID *= -1
    
    # Print Results
    print(f"{boardingPass}: row {myRow}, column {myColumn}, {seatClass}, seat ID {seatID}")
    return seatID
        
a = "0RRRBFFFBBF"
b = "1RRRFFFBBBF"
c = "0RLLBBFFBBF"
myBoardingPass = "0RLRBFBFFFF"

# Read from boarding passes, which is greatest value
total = 0
with open("2.txt", "r") as f:
    for x in f:
        total = max(abs(solver(x)), total)
        
solver(a)
solver(b)
solver(c)
solver(myBoardingPass)
print(f"Seat ID with the greatest absolute value: {total}")

# How is this problem similar to IEEE floating point representation (4 points)?
# This is similar on many ways such as how the boarding pass was partitioned to be processed and gave us the information needed and 
# how each chunk of bits were encoded and each chunk represented different things. Very similar to IEEE floating point representation