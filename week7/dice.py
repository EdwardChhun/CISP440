# Peter has 9 four-sided dice with faces 1,2,3,4
# Colin has 6 six-sided dice, with faces 1,2,3,4,5,6

# They roll all their dice and compare totals
# Win condition: highest total
# Result is drawn if totals are equal

# Q: What is the probability that Pete beats Colin

# Highest total is 36 for both
# Lowest total is 6 for colin, if he roles 1 for all 6 dice, 1/36 chance

# Find total ways to roll a sum of ranges

# Then compare the sums where pete has a total higher than colin

# Steps:
def ways_to_roll(dice, sides):
    dp = {0:1}
    
    # For every dice a person has
    for _ in range(dice):
        temp_dp = {}
        # Update the current dp with temp_dp
        # Looking for ways to roll a sum of "n" with "m" amount of dice
        for total, count in dp.items():
            for face in range(1, sides+1):
                # Initializing the dict if value isn't there
                if total + face not in temp_dp:
                    temp_dp[total + face] = 0
                temp_dp[total + face] += count
                
        dp = temp_dp
        # print(dp.items())
        
    return dp

# Pete
pete_wtr = ways_to_roll(9, 4)

# Colin
colin_wtr = ways_to_roll(6, 6)

pete_wins = 0
colin_wins = 0
tie = 0

for i in pete_wtr:
    for j in colin_wtr:
        count = pete_wtr[i] * colin_wtr[j]
        if i > j:
            pete_wins += count
        elif i < j:
            colin_wins += count
        else:
            tie += count
            
# The percent that pete wins over the overall chances
print(pete_wins)
print(colin_wins)
print(tie)
res = pete_wins / (pete_wins + colin_wins + tie)

print(f"If pete 9d4, colin 6d6: {round(res,7)}")

# Test case
pete_test = ways_to_roll(3, 4)
colin_test = ways_to_roll(2, 6)
pete_win_test = 0
colin_win_test = 0
tie_test = 0

for i in pete_test:
    for j in colin_test:
        count = pete_test[i] * colin_test[j]
        if i > j:
            pete_win_test += count
        elif i < j:
            colin_win_test += count
        else:
            tie_test += count

print(f"Test case: if pete has 3d4, and colin 2d6: {round(pete_win_test / (colin_win_test + pete_win_test + tie_test), 7)}")