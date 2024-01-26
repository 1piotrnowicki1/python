# Wygeneruj listę krotek (C, F), gdzie C, to temperatura w skali
# Celsjusza zmieniająca się od -20 do 100 stopni co 5 stopni, a F to
# odpowiadająca jej temperatura w skali Fahrenheita.

# (°C x 9/5) + 32 = °F

lista_krotek = [(c, (c*9/5)+32) for c in range(-20, 100, 5)]

print(lista_krotek)