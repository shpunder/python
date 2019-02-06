# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        shutil.copy(file_name, file_name + '.copy')
        print('Файл скопирован')
    except FileNotFoundError:
        print('файл {}  не найден'.format(file_name))
    except PermissionError:
        print('Невозможно создать копию или указан не файл')


def del_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        if input('Точно удалить y/n? ').lower() == 'y':
            os.remove(file_name)
            print('Файл удален')
    except FileNotFoundError:
        print('файл {} не найден'.format(file_name))


def change_dir():
    if not path_name:
        print("Необходимо указать путь файла вторым параметром")
        return
    try:
        os.chdir(path_name)
        show_path_current_dir()
    except FileNotFoundError:
        print('Путь {} не найден'.format(path_name))


def show_path_current_dir():
    print(os.getcwd())


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": del_file,
    "cd": change_dir,
    "ls": show_path_current_dir
}

try:
    dir_name = sys.argv[2]
    file_name = sys.argv[2]
    path_name = sys.argv[2]
except IndexError:
    dir_name = None
    file_name = None
    path_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
