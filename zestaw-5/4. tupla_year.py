# Utwórz krotkę miesiące=(styczeń, itd...). Wyświetl miesiące kolejnych
# kwartałów.


miesiace = ("styczen", "luty", "marzec", "kwiecien", "maj", "czer", "lip", "sier", "wrze", "paz", "lis", "grud")

for kwartal in range(0, len(miesiace), 3):
    print(miesiace[kwartal: kwartal + 3])     # zakres