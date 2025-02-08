import math                     # This is for factorial, I don't want to implement my own :)

def foo(blackTiles, coloredTiles) -> int:
    """ 
    blackTiles: the amount of empty space
    coloredTiles: the space of the colored tiles occupying the empty space
    """
    occupiedSpacePerColoredTile = coloredTiles
    result = 0
    coloredBlocks = 1           # The amount of coloredTiles in the system currently
    
    while blackTiles >= coloredTiles:
        
        n = (blackTiles - coloredTiles + coloredBlocks )
        r = blackTiles - coloredTiles
        
        # Using combinations, I'm treating the colored tiles occupying m-spaces as 1 single block
        # Essentially finding ways to reorder all the of the blocks in the system
        
        result += math.factorial(n) / (math.factorial(r) * math.factorial(n-r)) 
        
        coloredBlocks += 1                              # Adding another block
        coloredTiles += occupiedSpacePerColoredTile     # This can be treated as a terminal operation
                                                        # Trying to add another block to the system 
                                                        # If the coloredTiles occupied space exceeds
                                                        # The amount of black spaces available
                                                        # It will exit the while loop
    
    return result
    

if __name__ == "__main__":
    
    red = 2
    green = 3
    blue = 4
    
    total = 0
    total += foo(50, red)
    total += foo(50, green)
    total += foo(50, blue)
    print(total)