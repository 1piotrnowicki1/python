# Napisz program rozwiązujący zadania - zastosuj pętle for i while czy
# każda z nich daje dobre rozwiązanie?
#
# • Kupiec podczas swojej podróży handlowej do Wenecji podwoił
# tam swój początkowy kapitał, a następnie wydał 12 denarów. Po-
# tem udał się do Florencji, gdzie znowu podwoił liczbę posiadanych
# denarów i wydał 12 i ... został bez grosza. Ile denarów miał na po-
# czątku?

for i in range (0, 1000):
    s = i
    for n in range (0, 2):
        i = i*2
        i = i-12
    if i == 0:
        print(s)
        