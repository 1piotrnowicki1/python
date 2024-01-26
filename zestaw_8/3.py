#   3. Napisz funkcję sprawdzającą, ile razy dana liczba występuje wśród 20
#      elementów losowo wygenerowanej listy.

import random

liczba = int(input())


# wysta = 0



def check_number():
    randomlist = []
    wysta = 0

    for i in range(0, 20):
        n = random.randint(1, 100)
        randomlist.append(n)
    print(liczba)

    for n in randomlist:
        print(n)
        if n == liczba:
            wysta = wysta + 1

    print(wysta)
    return wysta
            # print(n)

# check_number()

print("liczba "+ str(liczba) + "wystąpiła: " + str(check_number()))
