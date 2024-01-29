#import random
from random import shuffle
def create(n): # sourcery skip
    numbers = list(range(1,n+1))
    while True:
        # je mélange la liste
        shuffle(numbers)
        sums = []
        try: # sourcery skip
            for i in range(len(numbers)):
                sums.append(numbers[i] + numbers[i+1])
        except IndexError:
            pass

        if len(sums) != len(set(sums)):
            pass
        else:
            return numbers

    #print(f"La liste est: {numbers}")

if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]

# for i in range(1,7):
#     print(i)

# s = list(range(1,6+1))
# print(s)

# 1 - je génère une liste aléatoire tant qu'elle ne satisfait pas les conditions
# 2 - je m'assur
# n = 15
# #print("n:", n)
# #random.seed(1337)
# #numbers = [random.randint(1, n) for _ in range(n)]
# # je dois en fait créer une liste ordonnée de 1 à n
# numbers = list(range(1,n+1))
# #print(numbers)

# # maintenant je parcours la liste
# while True:
#     # je mélange la liste
#     shuffle(numbers)
#     #print(f"Liste des nombres: {numbers}")
#     sommes = []
#     try: # sourcery skip
#         for i in range(len(numbers)):
#             sommes.append(numbers[i] + numbers[i+1])
#     except IndexError:
#         pass

#     # print(f"Liste des sommes: {sommes}") 
#     # print(set(sommes))
#     if len(sommes) != len(set(sommes)):
#         pass#print("There's at least one duplicate")  # recommence la boucle
#     else:
#         break
#     #print(set([7,6,10,7,4]))

# print(f"La liste est: {numbers}")


# s'il n'y a pas de doublon, je retourne la somme
# sinon je recommence
