# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys


def go_to_dir():
    dir_name = input("Ввдение название папки куда зайти: ")
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.chdir(dir_path)
    print(os.getcwd())


def current_files():
    print(os.listdir())


def delete_dir(dir_name):
    dir_name = input("Ввдение название новой папки: ")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print("директория {} удалена".format(dir_path))
    except NotImplementedError:
        print("директория {} не существует".format(dir_path))


def make_dir(dir_name):
    dir_name = input("Ввдение название новой папки: ")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("создана директория {}".format(dir_path))
    except FileExistsError:
        print("директория {} уже существует".format(dir_path))

print(
    "Выберите команду: \n1. Перейти в папку  \n2. Просмотреть содержимое текущей папки \n3. Удалить папку \n4. Создать папку"
)

do = input("Укажите действие: ")

if do == "1":
    go_to_dir()
elif do == "2":
    current_files()
elif do == "3":
    delete_dir()
elif d0 == "4":
    make_dir()

