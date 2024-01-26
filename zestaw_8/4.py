# 4. Napisz funkcję zwaracjącą indeksy elementów spośród 20 elementów
# losowo wygenerowanej tablicy równych wyszukiwanej wartości.

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

    for n in range(len(randomlist)):
        if randomlist[n] == liczba:
            indexy.append(n)
            print(n)
    print(indexy)

check_number()


    # for n in randomlist:
    #     print(n)
    #     if n == liczba:
    #         wysta = wysta + 1

    # print(wysta)
    # return wysta
            # print(n)