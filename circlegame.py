# # def create(n):
# #     order = [] #sourcery skip
# #     circle = list(range(1,n+1))
# #     i = 1
# #     while i < len(circle):
# #         order.append(circle[i])
# #         circle.pop(i)
# #         i += 1
# #     else:
# #         for index in range(len(circle)):
# #             if index == len(circle):
# #                 order.extend(circle)
# #                 break
# #             order.append(circle[index])
# #             circle.pop(index)
# #     return order

# # if __name__ == "__main__":
# #     print(create(1)) # [1]
# #     print(create(3)) # [2,1,3]
# #     print(create(7)) # [2,4,6,1,5,3,7]
    
    
# n = 4

# order = [] #sourcery skip
# circle = list(range(1,n+1))

# i = 1
# while i < len(circle):
#     order.append(circle[i])
#     circle.pop(i)
#     i += 1

# else:
#     #order.extend(circle)
#     #print(order)
#     for index in range(len(circle)):
#         if index == len(circle):
#             order.extend(circle)
#             break
#         order.append(circle[index])
#         circle.pop(index)
        
# print(order)

## Submitted working code (from GPT, i added the exception to make it work) ----------
def create(n):
    # Create a list representing the circle of players
    players = list(range(1, n + 1))
    
    # Initialize the result list to store the order of players leaving
    result = []

    # Start the elimination process
    while players:
        try:
            # Add the second player in the circle to the result list
            result.append(players[1])
            
            # Remove every second player from the circle
            players = players[2:] + players[:1]
        except IndexError:
            result.append(players[0])
            players.pop()

    return result

if __name__ == "__main__":
    for i in range(1,8):
        print(create(i))

## Course solution --------------
        

def create(n):
    turns = list(range(1, n+1))
    order = []

    i = 0
    while i < len(turns):
        if i%2 == 0:
            turns.append(turns[i])
        else:
            order.append(turns[i])
        i += 1
    return order


## My initial solution (don't work for all test cases, for example fails for n = 5) -------------
def create(n):
    order = [] 
    circle = list(range(1,n+1))
    cir = circle.copy()

    while circle:
        if len(circle) == 1:
            order.append(circle[0])
            circle.pop()
            break
        i = 1
        while i < len(circle):
            order.append(circle[i])
            circle.pop(i)
            i += 1
        else:
            last_element_index = cir.index(order[-1])
            element_suivant = cir[(last_element_index + 1) % len(cir)]
        
            if element_suivant in circle and element_suivant != circle[0]:
                circle = [circle[-1]] + circle[:-1]


    return order

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]
    print(create(4))
    
    
