# Napisz program wyznaczający ilość liczb w przedziale [1,100], [1,2000]
# podzielnych przez 7, które przy dzieleniu przez 2, 3, 4, 5, 6 dadzą resz-
# tę r = 1, w przypadku braku rozwiązania program powinien o tym
# informować.


liczby_4_range_1 = 0
liczby_4_range_2 = 0

range_1 = [x for x in range(1,101)]     #list comprehension
for liczba in range_1:
    if liczba%2 == 1 and liczba%3 == 1 and liczba%4 ==1 and liczba%5==1 and liczba%6==1 and liczba%7 ==0:
        liczby_4_range_1 += 1

if liczby_4_range_1 == 0:
    print("brak rozwiązania")
else:
    print(liczby_4_range_1)





