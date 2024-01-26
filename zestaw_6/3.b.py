
# Policz ile razy każdy wyraz występuje każdy wyraz w tym pliku.

f = open("nazwa.txt", "r")

lista = []

suma_slow = {}

for x in f:
    lista.append(x)

print(lista)

counter = 0



for i in range(len(lista)):
    print(lista[i])
    for j in range(len(lista)):
        if lista[j] == lista[i]:
            counter = counter + 1

    suma_slow[lista[i]] = counter  #dodaje do słownika


    counter = 0

print(suma_slow)