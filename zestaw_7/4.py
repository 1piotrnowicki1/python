# 4. Napisz kilka prostych funkcji:
#     • jest ujemna(liczba)
#     • jest parzysta(liczba)
#
#     • fibonacci
#         a. zwraca n-tą liczbę
#         b. zwraca wszystkie liczby aż do n = 100
#         c. zwraca sumę wszystkich liczb z przykładu b
#         d. A palindromic number reads the same both ways. The largest palin-
#            drome made from the product of two 2-digit numbers is 9009 = 91×99.
#            Find the largest palindrome made from the product of two3−digit numbers.

def ujemna(n):
    if n < 0:
        print("jest ujemna")

# ujemna(-1)


def parzysta(n):
    if n % 2 == 0:
        print("jest parzysta")
    else:
        print("nie")

# parzysta(0)


# -----------------------------------------------------------

# • fibonacci
#      b. zwraca wszystkie liczby aż do n = 100

#  • fibonacci
#      c. zwraca sumę wszystkich liczb z przykładu b


# n = int(input())

#
# def zliczaj():
#     a = 0
#     b = 1
#     suma = 0
#     for i in range(n):
#         print(a)
#         c = a + b
#         a = b
#         b = c
#         suma = suma + a
#         if a > n:
#             break
#     print(suma)
#
#
# zliczaj()

#         d. A palindromic number reads the same both ways. The largest palin-
#            drome made from the product of two 2-digit numbers is 9009 = 91×99.
#            Find the largest palindrome made from the product of two3−digit numbers.

# two digits
#
# def pal_two():
#     l1 = 0
#     l2 = 0
#     pal = 0
#     for i in range(10, 100):
#         for j in range(10, 100):
#             ilo = i*j
#             str_ilo = str(ilo)
#             if str_ilo[::-1] == str_ilo:
#                 # print(str_ilo)
#                 max_pal = int(str_ilo)
#                 if pal < max_pal:
#                     pal = max_pal
#                     l1 = i
#                     l2 = j
#
#     print(pal)
#     print(l1)
#     print(l2)
#
# pal_two()


# three digits
#
# def pal_3():
#     l1 = 0
#     l2 = 0
#     pal = 0
#     for i in range(100, 1000):
#         for j in range(100, 1000):
#             ilo = i*j
#             str_ilo = str(ilo)
#             if str_ilo[::-1] == str_ilo:
#                 # print(str_ilo)
#                 max_pal = int(str_ilo)
#                 if pal < max_pal:
#                     pal = max_pal
#                     l1 = i
#                     l2 = j
#     print(pal)
#     print(l1)
#     print(l2)
#
# pal_3()



# n digits input

digits = int(input())

def pal_3(n):

    l1 = 0
    l2 = 0
    pal = 0
    for i in range(10**(n-1), 10**n):
        for j in range(10**(n-1), 10**n):
            ilo = i*j
            str_ilo = str(ilo)
            if str_ilo[::-1] == str_ilo:
                # print(str_ilo)
                max_pal = int(str_ilo)
                if pal < max_pal:
                    pal = max_pal
                    l1 = i
                    l2 = j
    print(pal)
    print(l1)
    print(l2)

pal_3(digits)

