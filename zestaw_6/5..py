# Oblicz sumę wszystkich ujemnych elementów tablicy

lista = [1, -2, -3, 0, -1, -3]

suma = 0

for i in lista:
    print(i)
    if i < 0:
        suma = suma + i

print("suma wszystkich ujemanych elementów: " + str(suma))