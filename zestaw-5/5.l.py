# Utwórz słownik numery-alarmowe zawierający numer 112. Dodaj
# do słownika kilka numerów alarmowych ze strony
# https://www.uke.gov.pl/tablice-numerow-kierowania-alarmowego-
# nka-3223. Wypisz posortowaną zawartość tego słownika. Wykonaj
# kopię słownika. Wczytaj nazwę podaną z klawiatury i wypisz nu-
# mer alarmowy.

nr_alarmowe = {"policja": "997", "pogotowie": "999", "alarmowy": "112"}

# sotowanie po kluczu
nowy_klucze = print(sorted(nr_alarmowe.items()))

# sortowanie po wartosci
nowy_wartosci = print(sorted(nr_alarmowe.items(), key=lambda item: item[1]))

nazwa = input()


for key in nr_alarmowe.keys():
    if key == nazwa:
        print(nr_alarmowe[key])

