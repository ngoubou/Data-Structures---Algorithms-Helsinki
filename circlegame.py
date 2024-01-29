# def create(n):
#     order = [] #sourcery skip
#     circle = list(range(1,n+1))
#     i = 1
#     while i < len(circle):
#         order.append(circle[i])
#         circle.pop(i)
#         i += 1
#     order.extend(circle)
#     return order

# if __name__ == "__main__":
#     print(create(1)) # [1]
#     print(create(3)) # [2,1,3]
#     print(create(7)) # [2,4,6,1,5,3,7]
    
    
n = 7

order = [] #sourcery skip
circle = list(range(1,n+1))
# for i in range(len(circle)):
#     print(circle[i+1])
#cir = circle.copy()
# for i in range(len(cir)):
#     try:
#         order.append(circle[i+1]) # ajouter cet élément à la liste order
#         circle.pop(i+1)
#     except IndexError:
#         pass
# #print(circle[1:])

i = 1
while i < len(circle):
    order.append(circle[i])
    circle.pop(i)
    i += 1

else:
    #order.extend(circle)
    print(order)
    for index in range(len(circle)):
        if index == len(circle):
            order.extend(circle)
            break
        order.append(circle[index])
        circle.pop(index)
        
    print(order)
# for i in range(len(circle)):
#     if i < len(circle):
#         order.append(circle[i+1])
