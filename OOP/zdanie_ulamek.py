import math

class Ulamek:

    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def sprawdz_licznik(licznik):
        assert isinstance(licznik, int), 'licznik musi byc int'
        return

    def sprawdz_mianownik(mianownik):
        assert isinstance(mianownik, int), 'mianownik musi byc int'
        assert mianownik != 0, 'musi byc wieksze od 0'
        return

    def get_licznik(self):
        return self.licznik

    def get_mianownik(self):
        return self.mianownik

    def set_licznik(self, var):
        __class__.sprawdz_licznik(var)
        self.licznik = var
        return ""

    def set_mianownik(self, var):
        __class__.sprawdz_mianownik(var)
        self.mianownik = var
        return ""

    def __repr__(self):
        return f"Ułamek ma licznik {self.licznik}, a jego mianownik to {self.mianownik}"

    def __str__(self):
        return self.__repr__()

    def rownosc_ulamkow(self, other):

        wynik_1 = math.gcd(self.licznik, self.mianownik)
        wynik_2 = math.gcd(other.licznik, other.mianownik)

        self.licznik = self.licznik/wynik_1
        self.mianownik = self.mianownik/wynik_1

        other.licznik = other.licznik / wynik_2
        other.mianownik = other.mianownik / wynik_2

        return self.licznik == other.licznik and self.mianownik == other.mianownik


    def dodawanie_ulamkow(self, other):

        wspolny_mianownik = self.mianownik * other.mianownik

        self.licznik = self.licznik * other.mianownik
        other.licznik = other.licznik * self.mianownik
        suma_licznikow = self.licznik + other.licznik
        suma_licznikow = int(suma_licznikow)

        wspolny_mianownik = int(wspolny_mianownik)
        wynik_1 = math.gcd(suma_licznikow, wspolny_mianownik)
        suma_licznikow = suma_licznikow / wynik_1
        suma_licznikow = int(suma_licznikow)
        wspolny_mianownik = wspolny_mianownik / wynik_1
        wspolny_mianownik = int(wspolny_mianownik)

        return Ulamek(suma_licznikow, wspolny_mianownik)

    def mnożenie_ułamków(self, other):

        new_licznik = self.licznik * other.licznik
        new_licznik = int(new_licznik)

        new_minownik = self.mianownik * other.mianownik
        new_minownik = int(new_minownik)

        wynik_new = math.gcd(new_licznik, new_minownik)

        new_licznik = new_licznik / wynik_new
        new_licznik = int(new_licznik)

        new_minownik = new_minownik / wynik_new
        new_minownik = int(new_minownik)

        return Ulamek(new_licznik, new_minownik)


ulamek_1 = Ulamek(6,2)
ulamek_2 = Ulamek(2,2)


# print(ulamek_1.rownosc_ulamkow(ulamek_2))
# print(ulamek_1.dodawanie_ulamkow(ulamek_2))
print(ulamek_1.mnożenie_ułamków(ulamek_2))


# prównaj ułamki z wykorzystaniem magnicznich metod