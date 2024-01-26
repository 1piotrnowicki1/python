# jest podzielna przez 4 i niepodzielna przez 100
# lub jest podzielna przez 400

# Wygeneruj listę lat przestępnych.

lata_przestepne = [x for x in range(0, 2022) if x%400 == 0 or x%4 == 0 and x%100 != 0]

print(lata_przestepne)