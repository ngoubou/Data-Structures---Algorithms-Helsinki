n = 5

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
    last_element_index = cir.index(order[-1])
    # Trouver l'élément suivant 
    element_suivant = cir[(last_element_index + 1) % len(cir)]
    # si l'élément après le dernier nombre mis dans la liste order
    # n'est pas en 1e position dans la liste circle, mets le en 1e position et conserve le reste
    if element_suivant in circle and element_suivant != circle[0]:
        circle = [circle[-1]] + circle[:-1]
    
    
print(order)

# def best_profit(prices):
#     n = len(prices)
#     best = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             best = max(best, prices[j] - prices[i])
#     return best

def best_profit(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        min_price = min(prices[:i+1])
        best = max(best, prices[i] - min_price)
    return best

prices = [3,7,5,1,4,6,2,3]
print(best_profit(prices))