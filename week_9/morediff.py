def create(n):
    if n == 1:
        return [1]
    elif n == 2 or n == 3:
        return None
    else:
        result = []
        for i in range(1, n + 1, 2):
            result.append(i)
        for i in range(2, n + 1, 2):
            result.append(i)
        return result

if __name__ == "__main__":
    print(create(1))  # [1]
    print(create(2))  # None
    print(create(3))  # None
    print(create(4))  # [1, 3, 2, 4]
    print(create(7))  # [1, 3, 5, 7, 2, 4, 6]
