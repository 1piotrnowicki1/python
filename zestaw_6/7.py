# Utwórz listę (słownik, krotkę - wybierz strukturę) artykułów dwóch
# supermarketów wraz z cenami. Pobieraj dane z klawaitury i sprwadź
#   • czy można kupić podany artykuł
#   • który z supermarketów zawiera podany artykuł
#   • gdzie nie kupisz danego produktu,
#   • czy można kupić ten artykuł w dowlnym supermarkecie



mar_1 = {"chleb": 2, "papier": 3, "ksiazka": 10, "maslo": 1}

mar_2 = {"maslo": 1, "zapalki": 5, "kredki": 8}

znajdz = input()
flaga_1 = 0
flaga_2 = 0

for key in list(mar_1.keys()):
    if key == znajdz:
        print("Tak, " + znajdz + " produkt jest dostępny w markecie 1")
        flaga_1 = 1

for key in list(mar_2.keys()):
    if key == znajdz:
        print("Tak, " + znajdz + " produkt jest dostępny w markecie 2")
        flaga_2 = 1

if flaga_1 == 0:
    print(znajdz + " nie kupisz w markecie 1")

if flaga_2 == 0:
    print(znajdz + " nie kupisz w markecie 2")


if flaga_1 == 1 and flaga_2 == 1:
    print(znajdz + " można kupic w dowolnym markecie")
else:
    print(znajdz + " nie można kupic w dowolnym markecie")