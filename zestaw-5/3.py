# Wykonaj różne rodzaje kopii poniższej listy:
# lista=[”Napis”,1234,[”Słowo”,5678]].

import copy


lista = ["Napis", 1234, ["Słowo", 5678]]

lista_1 = copy.deepcopy(lista)
print("Lista_0: ", "Value: ", lista)
print("Lista_1: ", "Value: ", lista_1)

lista_2 = copy.copy(lista)

print("Lista_2: ", "Value: ", lista_2)

lista[2][1] = 2022

print("Lista_0: ", "Value: ", lista)
print("Lista_1: ", "Value: ", lista_1)
print("Lista_2: ", "Value: ", lista_2)