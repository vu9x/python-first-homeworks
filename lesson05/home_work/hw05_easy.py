# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
import sys
import shutil


def make_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("создана директория {}".format(dir_path))
    except FileExistsError:
        print("директория {} уже существует".format(dir_path))


def delete_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print("директория {} удалена".format(dir_path))
    except NotImplementedError:
        print("директория {} не существует".format(dir_path))


for f in range(1, 10):
    make_dir("dir_{}".format(f))
    delete_dir("dir_{}".format(f))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for f in os.listdir(os.getcwd()):
    if os.path.isdir(os.path.join(os.getcwd(), f)):
        print("Папка {} содержит директорию {}".format(os.getcwd(), f))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print(os.listdir())
print(sys.argv[0])
# current_file = sys.argv[0]
# current_file_list = current_file.split("/")
# current_file_name = current_file_list[-1]
# current_file_name.split(.)

new_file_name = "copied_file.py"
shutil.copyfile(sys.argv[0], os.path.join(os.getcwd(), new_file_name))

