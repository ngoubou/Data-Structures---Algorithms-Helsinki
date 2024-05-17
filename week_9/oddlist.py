def count(n, x):
    # Base case: If n is 1, there's only one possible list, which is [x]
    if n == 1:
        return 1
    # Base case: If n is 2 and x is 1, there are two possible lists: [1, 2] and [2, 1]
    elif n == 2 and x == 1:
        return 2
    # Base case: If n is 2 and x is not 1, there's only one possible list: [x, 1]
    elif n == 2:
        return 1
    else:
        # If x is the first element, the next element can be any number except x
        if x == 1:
            return count(n-1, x) + count(n-1, x+1)
        # If x is the last element, the previous element can be any number except x
        elif x == n:
            return count(n-1, x-1)
        # For any other case, the next or previous element can be any number adjacent to x
        else:
            return count(n-1, x-1) + count(n-1, x+1)

if __name__ == "__main__":
    print(count(1, 1))  # Output: 1
    print(count(4, 2))  # Output: 4
    print(count(8, 5))  # Output: 830

# Do not work