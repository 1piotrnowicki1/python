# Utwórz listę krotek zawierającą imiona i nazwiska. Wypisz inicjały.

lista_imion = [("Tomek", "Len", "2"), ("Lena", "Antek", "3"), ("Marta", "Młyn", "8"), ("Aneta", "Zatem", "9")]

nowa_lista = [(x[0][0], x[1][0], x[2]) for x in lista_imion]

print(nowa_lista)