# Utwórz listę imion osób z Twojej grupy, a następnie wypisz najdłuższe,
# najkrótsze imię. Posortuj listę. Program nie uwzglednia wielkości liter
# oraz usuwa wpisane przypadkowo spacje (funkcje upper i split)

names = ["Piotr", "Tomasz", "Katarzyna", "Jan", "As"]
max = 0
min = 1000
imie = names[0]
imie_min = names[0]

for i in range (len(names)):
    if len(names[i]) > max:
        max = len(names[i])
        print("max: ", max)
        imie = names[i]
        print("imie: " + imie)

for i in range(len(names)):
    if len(names[i]) < min:
        min = len(names[i])
        print("min: ", min)
        imie_min = names[i]
        print("imie_min: ", imie_min)


print("najdłuzsze imię: " + imie)
print("najkrótsze imię: " + imie_min)