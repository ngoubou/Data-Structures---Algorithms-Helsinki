def find(t):
    for i in list(set(t)):
        if t.count(i) == 1:
            return i

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5

# i find the unique values in the list by converting it to a set
# i then go through the set (i do it cause it has less values than the entire list, which means less steps in my loop)
# and check if each number in the set appears once in the list
    
## Course solution --------
# The following solution finds the minimum and the maximum values on the list, which must be two different numbers. Then it checks, which of the two numbers occurs only once.
    
def find(t):
    number1 = min(t)
    number2 = max(t)
    if t.count(number1) == 1:
        return number1
    else:
        return number2

# Below is another solution that goes through the list and returns a number that occurs only once. 
# By keeping track of the last number in a variable other, the algorithm ensures that the method count is called at most twice.

def find(t):
    other = None
    for x in t:
        if x == other:
            continue
        if t.count(x) == 1:
            return x
        other = x