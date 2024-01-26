# Utwórz listę imion. Wypisz imiona i ich pierwsze litery

lista_imion = ["Tomek", "Lena", "Marta", "Aneta", "Jarek"]

nowa_lista = [(x, x[0]) for x in lista_imion]

print(nowa_lista)