def create(t):
    subsets_sum = [0]  # Initialize with 0 as the sum of an empty subset
    for num in t:
        new_sums = [num + s for s in subsets_sum]  # Calculate new sums by adding the current number to all previous subset sums
        subsets_sum.extend(new_sums)  # Add new sums to the list of subset sums
    subsets_sum.sort()  # Sort the list of subset sums in ascending order
    return subsets_sum

if __name__ == "__main__":
    print(create([1, 2, 3]))   # Expected output: [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337]))  # Expected output: [0, 42, 1337, 1379]
    print(create([1, 1, 1]))   # Expected output: [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5]))         # Expected output: [0, 5]
