# def count(x):
#     # Calculate the total number of coins needed for each denomination
#     num_coins_5 = x // 5
#     num_coins_4 = (x % 5) // 4
#     num_coins_1 = (x % 5) % 4

#     # Return the total count of coins
#     return num_coins_5 + num_coins_4 + num_coins_1

def count(x):
    return x//5 + [0, 1, 1, 1, 1][x%5]

# Example usage
if __name__ == "__main__":
    print(count(2)) # Expected output: 2
    print(count(8))  # Expected output: 2
    print(count(12345))  # Expected output: 2469
    print(count(1337**9))  # Expected output: 2730314408854633746890878156
