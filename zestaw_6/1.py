# Katalogi i pliki
#   • Wyświetl ścieżkę katalogu domowego aktualnie zalogowanego użyt-
#       kownika.
#   • Wyświetl zawartość w/w katalogu.
#   • Utwórz listę plików (katalogów) z w/w katalogu.
#   • Wyświetl listę plików ”pythona” z w/w katalogu.
#   • Wypisz wszystkie pliki zaczynajace się na podaną literę z klawia-
#       tury z w/w katalogu.

# https://csatlas.com/python-os-user-home-directory/


# -------------------------------------------------------

import os

# Wyświetl ścieżkę katalogu domowego aktualnie zalogowanego użytkownika.

# from pathlib import Path
#
# home_dir = Path.home()
#
# print( f'Path: { home_dir } !' )

# ----------------------------------------------------


# # Wyświetl zawartość w/w katalogu.
#
# # importing os module
# import os
#
# # Get the list of all files and directories
# # in the root directory
# path = input()
# dir_list = os.listdir(path)
#
# print("Files and directories in '", path, "' :")
#
# # print the list
# print(dir_list)
# print(path)
#
#
# ------------------------------------------------------

# Wyświetl zawartość w/w katalogu. I posortuj pliki i katalogi
#
#
# from os.path import isfile
# import os
#
# # Get the list of all files and directories
# # in the root directory
# path = "/home/piotr/python_lekcje/"
# dir_list = os.listdir(path)
#
#
# # print the list
# print(dir_list)
#
# files = []
# dirs = []
#
# for i in dir_list:
#     isFile = os.path.isfile(path + i)
#     # print(i)
#     print(isFile)
#
#     if isFile == 1:
#         files.append(i)
#     else:
#         dirs.append(i)
#
# print(files)
# print(dirs)


# ------------------------------------------------

# Wyświetl listę plików ”pythona” z w/w katalogu.
#
#
# from os.path import isfile
# import os
#
# # Get the list of all files and directories
# # in the root directory
# path = "/home/piotr/python_lekcje/"
# dir_list = os.listdir(path)
#
#
# # print the list
# print(dir_list)
#
# files = []
# dirs = []
# py_files = []
#
# for i in dir_list:
#     isFile = os.path.isfile(path + i)
#     # print(i)
#     print(isFile)
#
#     if isFile == 1:
#         files.append(i)
#     else:
#         dirs.append(i)
#
# print(files)
# print(dirs)
#
# for f in files:
#     if f.endswith('.py'):
#         print("jest plikiem .py: " + f)
#         py_files.append(f)
#     else:
#         print("NIE jest plikiem .py: " + f)
#
# print(py_files)
#
# -----------------------------------------

# Wypisz wszystkie pliki zaczynajace się na podaną literę z klawiatury z w/w katalogu.