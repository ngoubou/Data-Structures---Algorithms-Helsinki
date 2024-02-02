from random import shuffle
# def create(n): # sourcery skip
#     numbers = list(range(1,n+1))
#     while True:
#         shuffle(numbers)
#         sums = []
#         try: 
#             for i in range(len(numbers)):
#                 sums.append(numbers[i] + numbers[i+1])
#         except IndexError:
#             pass

#         if len(sums) == len(set(sums)):
#             return numbers


# if __name__ == "__main__":
#     print(create(6)) # [3, 1, 6, 2, 4, 5]
#     print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
#     print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]

# My code used too much time for processing the input.
# It failed with the input 24
# Certainly because of the while loop
#print(create(6))

def create(n):
    return list(range(1,n+1))

# Turns out the solution was much more simpler 