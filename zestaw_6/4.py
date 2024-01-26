# Oblicz długość najdłuższego fragmentu tablicy, w którym wszystkie
# elementy są dodatnie.


tab = [1, 1, 1, 2, 1, -1, 1, 1, 2, 3]


dl = 0
ram = 0

tab.append(-1)
print(tab)

for i in tab:
    if i > 0:
        dl = dl + 1
    else:
        if dl > ram:
            ram = dl
        dl = 0

print(ram)
