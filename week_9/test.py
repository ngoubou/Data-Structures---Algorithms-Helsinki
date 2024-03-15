# def count(x):
#     # Calculate the total number of coins needed for each denomination
#     num_coins_5 = x // 5
#     num_coins_2 = (x % 5) // 2
#     num_coins_1 = (x % 2) // 1

#     # Return the total count of coins
#     return num_coins_5 + num_coins_2 + num_coins_1

# if __name__ == "__main__":
#     print(count(13)) # 4
#     print(count(12345)) # 2469
#     print(count(1337**9)) # 2730314408854633746890878156

## Course solution ----
    
# Since the optimal solution includes as many coins of value 5 as possible, the number such coins is exactly \lfloor x/5 \rfloor$. This can be computed efficiently without adding coins individually.
# The number of coins of value 1 and 2 depends on the remainder of dividing x by 5.
# def count(x):
#     return x//5 + [0, 1, 1, 2, 2][x%5]

def count(x):
    # Define the new coin values
    coin_values = [1, 4, 5]

    # Calculate the minimum number of coins needed
    min_coins = x // 5  # Use integer division for 5-value coins
    remainder = x % 5

    # Adjust for 4-value coins
    if remainder == 4:
        min_coins += 2  # Use two 2-value coins instead of one 4-value coin
    else:
        min_coins += remainder  # Use remaining 1-value or 2-value coins

    return min_coins
# if __name__ == "__main__":
#     print(count(13)) # 4
#     print(count(12345)) # 2469
#     print(count(1337**9)) # 2730314408854633746890878156

print([0, 1, 1, 2, 2][3])