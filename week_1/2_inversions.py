"""
Inversions
https://cses.fi/dsa24k/task/3049
"""

def count(t: list):
    """Count the total number of inversions in a list."""
    inv = 0
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if (i < j) and t[i] > t[j]:
                inv += 1
    return inv

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12

