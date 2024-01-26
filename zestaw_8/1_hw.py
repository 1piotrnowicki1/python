# Napisz funkcję sprawdzającą, czy dana liczba jest potęgą innej liczby
# całkowitej i różnej od zera.


liczba = int(input())

l_potega = int(input())


def sprawdz(liczba, l_potega):
    for l in range(l_potega):
        if liczba**l == l_potega:
            print("TRUE: " + str(l))
            break
        else:
            print("FALSE")


sprawdz(liczba, l_potega)