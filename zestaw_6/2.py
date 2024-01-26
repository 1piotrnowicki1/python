# Utwórz słownik zawierający jako klucze krotki (imiona i nazwiska),
# a wartościami są numery indeksów. Sprawdź czy osoba znajduje się
# w słowniku. Wypisz jej numer indeksu.


slo = {("Piotr", "Nowicki"): "000111", ("Tom", "John"): "0002"}

znajdz = input()


# print(znajdz)

for key in list(slo.keys()):
    # print(key)

    if znajdz == key[0] or znajdz == key[1]:
        print(slo[key])























