# Utwórz listę imion wypisz tyllko te zakończone na literę ”a”.

lista_imion = ["Tomek", "Lena", "Marta", "Aneta", "Jarek"]

nowa_lista = [(x, x[-1]) for x in lista_imion if x[-1] != "a"]

print(nowa_lista)