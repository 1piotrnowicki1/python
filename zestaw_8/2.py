# 2. Napisz funkcję sprawdzajcą, czy dana liczba występuje wśród 20 ele-
# mentów losowo wygenerowanej listy - wyszukiwanie sekwencyjne i wy-
# szukiwanie binarne.


import random

liczba = int(input())

def check_number():
    randomlist = []
    # wysta = 0
    indexy = []

    for i in range(0, 20):
        n = random.randint(1, 10)
        randomlist.append(n)
    print(randomlist)
    return randomlist

def check_sek():
    lista = check_number()
    for n in lista:
        if n == liczba:
            print("liczba zostala znaleziona")
            break

def check_binar():
    sort_lista = check_number()
    sort_lista.sort()
    print(sort_lista)
    p = -1
    L = ip = 0
    ik = len(sort_lista) - 1

    while (ip <= ik):
        L = L + 1
        isr = (ip + ik) >> 1
        if (sort_lista[isr] == liczba):
            p = isr
            break
        elif (liczba < sort_lista[isr]): ik = isr - 1
        else:
            ip = isr + 1
    print(p)

check_sek()

check_binar()