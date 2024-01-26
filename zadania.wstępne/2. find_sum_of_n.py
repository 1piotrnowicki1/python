# Znajdź sumę n liczb postaci 1 + 22 + 333 + 4444 + ....
# Dla n = 4 suma = 1 + 22 + 333 + 4444
# dla n = 6 suma = 1 + 22 + 333 + 4444 + 55555 + 666666


n = int(input("Podaj liczbę n: "))
suma = 0

for i in range (1, n+1):
    suma = suma + int(i*str(i))    #  * powiel znak

print(suma)