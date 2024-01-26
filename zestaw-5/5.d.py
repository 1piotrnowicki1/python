# Wygeneruj listę krotek (x, y) przy czym x  != y x, y ∈ [0, 20].

lista_krotek =[(x, y) for x in range(0, 20) for y in range(0, 20) if x != y]


print(lista_krotek)
