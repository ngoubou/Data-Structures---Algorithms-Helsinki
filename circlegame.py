# def create(n):
#     order = [] #sourcery skip
#     circle = list(range(1,n+1))
#     i = 1
#     while i < len(circle):
#         order.append(circle[i])
#         circle.pop(i)
#         i += 1
#     else:
#         for index in range(len(circle)):
#             if index == len(circle):
#                 order.extend(circle)
#                 break
#             order.append(circle[index])
#             circle.pop(index)
#     return order

# if __name__ == "__main__":
#     print(create(1)) # [1]
#     print(create(3)) # [2,1,3]
#     print(create(7)) # [2,4,6,1,5,3,7]
    
    
n = 4

order = [] #sourcery skip
circle = list(range(1,n+1))

i = 1
while i < len(circle):
    order.append(circle[i])
    circle.pop(i)
    i += 1

else:
    #order.extend(circle)
    #print(order)
    for index in range(len(circle)):
        if index == len(circle):
            order.extend(circle)
            break
        order.append(circle[index])
        circle.pop(index)
        
print(order)
