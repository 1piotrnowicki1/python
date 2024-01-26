# Wczytaj liczbę, a następnie wypisz jej cyfry słownie.
# Przykład: *********0
# - „zero ̋, ******-147 - ̋minus jeden cztery siedem ̋.

liczba = input()

dict = {"0": "zero", "1": "jedne", "2": "dwa", "3": "trzy", "4": "cztery", "-": "minus"}

for number in liczba:
    print(dict[number])

