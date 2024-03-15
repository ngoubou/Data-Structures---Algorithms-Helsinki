def count(x):
    # Calculate the total number of coins needed for each denomination
    num_coins_5 = x // 5
    num_coins_2 = (x % 5) // 2
    num_coins_1 = (x % 5) % 2

    # Return the total count of coins
    return num_coins_5 + num_coins_2 + num_coins_1

if __name__ == "__main__":
    print(count(13)) # 4
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156

## Course solution ----
    
# Since the optimal solution includes as many coins of value 5 as possible, the number such coins is exactly \lfloor x/5 \rfloor$. This can be computed efficiently without adding coins individually.
# The number of coins of value 1 and 2 depends on the remainder of dividing x by 5.
def count(x):
    return x//5 + [0, 1, 1, 2, 2][x%5]
    