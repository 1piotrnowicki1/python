# Napisz program, sprawdzający czy w danym pliku znajduje się poszu-
# kiwany wyraz. Jeśli tak wypisz ile razy został wyszukany.




# f = open("nazwa.txt", "r")         #czytaj plik, pierwszą linie
# print(f.readline())

slowa = input()

f = open("nazwa.txt", "r")

lista = []

for x in f:
    lista.append(x)
    # print(x)
print(lista)

counter = 0

for i in range(len(lista)):
    if lista[i] == slowa:
        counter = counter + 1

print(counter)

if counter > 0:
    print("słowo dodane: " + str(counter))
else:
    print("brak słowa")