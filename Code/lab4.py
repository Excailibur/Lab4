import sys

with open("Data/rosalind_ba5a.txt", "r") as file:
# Read the entire file content
    money = int(file.readline().strip("\n"))
    coins = [int(c) for c in file.readline().strip("\n").split(",")]

sys.setrecursionlimit(30000)
memo = {}

# Find the minimum number of coins needed to make up the amount
'''
    amount: the amount of money to make up
    coinDenom: the denominations of the coins
    arraySize: the size of the coinDenom array
'''
def FindMinCoins(amount, coinDenom, arraySize):
    # Base case: if the amount is 0, return 0
    if amount == 0:
        return 0
    
    # If subproblem is already solved, return the result from DP table
    if amount in memo:
        return memo[amount]
    
    # Initialize the minimum number of coins needed to make up the amount
    minCoins = sys.maxsize

    # Find the minimum number of coins needed to make up the amount
    for i in range(0, arraySize):
        if coinDenom[i] <= amount:
            currentMin = FindMinCoins(amount - coinDenom[i], coinDenom, arraySize)
            if currentMin + 1 < minCoins and currentMin != sys.maxsize:
                minCoins = currentMin + 1
    
    memo[amount] = minCoins

    return minCoins

print(coins)

print(FindMinCoins(money, coins, len(coins)))