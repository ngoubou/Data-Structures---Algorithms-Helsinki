def count(s): # sourcery skip
    char_list = ["t", "i", "r", "a"] 
    substrings = []
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            substrings.append(substring)

    count = 0
    for string in substrings:
        if all(char in string for char in char_list):
            count += 1
           
    return count


if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4
    print(count("ttrira")) # 2

# Memory error for input "tira"*(10**5)
## Course solution --------
