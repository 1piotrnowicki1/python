# Utwórz słownik zawierający jako klucze krotki (imiona i nazwi-
# ska), a wartości to numery telefonów. Wypisz dane ze słownika
# - imiona, nazwiska i numer telefonu. Wypisz inicjały i numery
# telefonów.

dict = {("Piotr", "Nowicki"): "0323233", ("Pawel", "Zowy"): "02222233", ("Roman", "Wac"): "111111"}

# klucze
for key in dict.keys():
    print(key[0][0], key[1][0], dict[key])


# wartości
for value in dict.values():
    print(value)

for value in dict.items():
    print(value)