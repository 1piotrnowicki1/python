# Utwórz słownik zawierający jako klucze krotki (imiona i nazwi-
# ska), a wartościami są daty urodzenia. Wypisz osoby urodzone w
# roku podanym z klawiatury (urodzone później niż wskazuje rok
# podany z klawiatury).

dict = {("Piotr", "Nowicki"): "20.02.2000", ("Pawel", "Zowy"): "23.01.1933", ("Roman", "Wac"): "11.10.1999"}

rok_input = input()

# print(rok_input)

for key in dict.keys():
    if rok_input == dict[key][-4:] or rok_input < dict[key][-4:]:
        print(key)
    else:
        print("brak daty")