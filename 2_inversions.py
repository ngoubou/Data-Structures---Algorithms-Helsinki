"""
Inversions
https://cses.fi/dsa24k/task/3049
"""

def count(t: list):
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

# inv = 0
# new_var = [1,8,2,7,3,6,4,5]
# # for indices,values in enumerate(new_var):
# #     try:
# #         if (indices < indices + 1) and new_var[indices] > new_var[indices + 1]:
# #             inv += 1
# #     except IndexError:
# #         pass

# for i in range(len(new_var)):
#     #print(f"valeur de i: {i}")
#     for j in range(i+1,len(new_var)):
#         if (i < j) and new_var[i] > new_var[j]:
#             inv += 1
#         #print(f"valeur de j: {j}")
# print(inv)