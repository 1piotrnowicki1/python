# Napisz trzy funkcje:
#   • hw1 nie przyjmującą żadnych argumentów i zwracającą ciąg zna-
#       ków ’Hello, World!’;
#   • hw2 nie przyjmującą żadnych argumentów i nie zwracającą też
#       nic, ale drukującą na standardowe wyjście ’Hello, World!’
#   • hw3 przyjmującą dwa argumenty i drukującą na standardowe wyjście
#       oba argumenty oddzielone przecinkiem. Przetestuj te funkcje za pomocą:
#       • print hw1()
#       • hw2()
#       • hw3(’Hello’, ’World!’)


# Napisz funkcje:
# • hw1 nie przyjmującą żadnych argumentów i zwracającą ciąg znaków ’Hello, World!’;

def hw1():
    return "Hello, World!"

# --------------------------------------------------------------

# Napisz funkcje:
# • hw2 nie przyjmującą żadnych argumentów i nie zwracającą też nic,
#   ale drukującą na standardowe wyjście ’Hello, World!’

def hw2():
    print("Hello, World!")


# --------------------------------------------------------------

# Napisz funkcje:
#   • hw3 przyjmującą dwa argumenty i drukującą na standardowe wyjście
#       oba argumenty oddzielone przecinkiem. Przetestuj te funkcje za pomocą:
#       • print hw1()
#       • hw2()
#       • hw3(’Hello’, ’World!’)

def hw3(liczba1, liczba2):
    print("Liczba1 =  " + liczba1 + ",    Liczba2 =  " + liczba2)




hw3("3", "4")

print(hw1())

hw2()


