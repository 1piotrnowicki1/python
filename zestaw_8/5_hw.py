# Masz dane listę państw i listę odpowiadających im miast (stolic). Za-
# proponuj strukturę danych i napisz program - grę w której losujemy jed-
# no państwo i oczekujemy podania jego stolicy. Program powinien mieć
# możliwość dodania nowego państwa i jego stolicy, zliczania punktów
# i informwania gracza o jego wyniku. Grcz decyduje o ilości powtórzeń.


lista_panstw = {"Polska": "Gdansk", "Szwecja": "Goteburg", "Anglia": "London", "Niemcy": "Berlin"}

point = 0

while True:

    print("wybierz opcje 1: zagraj")
    print("wybierz opcje 2: dodaj panstwo")
    print("wybierz opcje 3: zakoncz")

    Podaj_opcje = int(input())

    if Podaj_opcje == 1:
        for key in lista_panstw:
            print(key)
            sprawdz_panstwo = input("Podaj stolice tego Panstwa: ")
            if lista_panstw[key] == sprawdz_panstwo:
                print("Dobrze, zdobyłem punkt")
                point = point + 1
            else:
                print("Zle nie zdobywasz pkt")
        print("Zdobyłeś " + str(point) + " pkt")

    elif Podaj_opcje == 2:
        print("Podaj panstwo: ")
        dodaj_panstwo = str(input())
        print("Podaj miasto: ")
        dodaj_miasto = str(input())

        lista_panstw[dodaj_panstwo] = dodaj_miasto
        print("nowa lista państwa: " + str(lista_panstw))

    elif Podaj_opcje == 3:
        print("progam skonczony")
        break


# Zadanie domowe
#
# wersja_1 z losowaniem:
# losuj wszystkie pyania o Panstwa w różnej kolejności
#
# wersja_2 z losowaniem
# zapytaj np. o cztery panstwa