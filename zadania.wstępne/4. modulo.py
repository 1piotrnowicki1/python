# Napisz program wyznaczający największą liczbę podzielną przez 7,
# która przy dzieleniu przez 2, 3, 4, 5, 6 daje resztę r = 1.

# największa
for liczba in range (10000, 0, -1):
    if liczba%2 == 1 and liczba%3 == 1 and liczba%4 ==1 and liczba%5==1 and liczba%6==1 and liczba%7 ==0:
        print(liczba)
        break

print(301%4)

# Najmniejsza
# for liczba in range (0, 10000):
#     if liczba%2 == 1 and liczba%3 == 1 and liczba%4 ==1 and liczba%5==1 and liczba%6==1 and liczba%7 ==0:
#         print(liczba)
#         break
#
# print(301%4)