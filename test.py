def create(n): # sourcery skip
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
    #print(create(4))
    
    
# n = 7

# order = [] # sourcery skip
# circle = list(range(1,n+1))
# cir = circle.copy()

# while circle:
#     if len(circle) == 1:
#         order.append(circle[0])
#         circle.pop()
#         break
#     i = 1
#     while i < len(circle):# sourcery skip
#         order.append(circle[i])
#         circle.pop(i)
#         i += 1

#     else:
#         #print()
#         # trouver l'index de order[-1] dans cir
#         last_element_index = cir.index(order[-1])
#         # Trouver l'élément suivant 
#         element_suivant = cir[(last_element_index + 1) % len(cir)]
#         # si l'élément après le dernier nombre mis dans la liste order
#         # est dans la liste circle, mets le en 1e position et conserve le reste
#         # if element_suivant in circle:
#         #     new_circle = [circle[-1]] + circle[:-1]
#         # si l'élément après le dernier nombre mis dans la liste order
#         # n'est pas en 1e position dans la liste circle, mets le en 1e position et conserve le reste
#         if element_suivant in circle and element_suivant != circle[0]:
#             circle = [circle[-1]] + circle[:-1]
    
    
# print(order)
# i = 1
# while i < len(circle):
#     order.append(circle[i])
#     circle.pop(i)
#     i += 1
# print()

# si ce n'est pas le cas, le 1er élément de cir devient l'élément 1 de circle
# # else:
# #     cir.extend(circle)
# #     #i = 1
# #     while i < len(cir):
# #         i += 2
# #         order.append(cir[i])
# #         circle.pop(i)
# #     order.extend(circle)
#     # for index in range(len(circle)):
#     #     if index == len(circle):
#     #         order.extend(circle)
#     #         break
#     #     order.append(circle[index])
#     #     circle.pop(index)
        
# #print(order)

# while len(circle) > 0:
#     if i <= len(circle):
#         order.append(circle[i])
#         circle.pop(i)
#         i += 1
#     else:
#         i

# def rotate_circular(elements, steps):
#     # Perform a circular rotation by manipulating indices
#     steps = steps % len(elements)
#     return elements[-steps:] + elements[:-steps]

# # Example usage
# original_elements = [1, 2, 3, 4]

# # Rotate the circular structure
# rotated_elements = rotate_circular(original_elements, 0)
# print(rotated_elements)
# # # Append a new element (assuming it's a queue-like behavior)
# # rotated_elements.append(6)

# # # Pop an element (assuming it's a queue-like behavior)
# # removed_element = rotated_elements.pop()

# # # Print the resulting circular structure
# # print(rotated_elements)
# # print("Removed Element:", removed_element)

# for i in range(1,len(circle)-1):
#     #print(i)
#     order.append(cir[i])
#     cir.pop(i)
