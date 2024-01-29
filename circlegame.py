n = 3

order = [] #sourcery skip
circle = list(range(1,n+1))
# for i in range(len(circle)):
#     print(circle[i+1])
cir = circle.copy()
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


order.extend(circle)
print(order)
# for i in range(len(circle)):
#     if i < len(circle):
#         order.append(circle[i+1])
