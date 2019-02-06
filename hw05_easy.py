# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        return True
    else:
        return False


def remove_dir(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        return True
    else:
        return False


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folder(path_name):
    print(os.listdir(path_name))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(file_name):
    shutil.copy(file_name, file_name + '.copy')


if __name__ == '__main__':
    while True:
        choice = input('Выберите пункт:\n'
                       '1. Создать папки\n'
                       '2. Удалить папки\n'
                       '3. Показать папки\n'
                       '4. Копия скрипта\n'
                       '5. Выход\n'
                       '---------------------\n'
                       'Ваш выбор:')
        if choice == '1':
            for i in range(10):
                create_dir('dir_' + str(i))
        if choice == '2':
            for i in range(10):
                remove_dir('dir_' + str(i))
        if choice == '3':
                show_folder(os.getcwd())
        if choice == '4':
                copy_file(__file__)
        if choice == '5':
            break
