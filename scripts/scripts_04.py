# Создать скрипт. Программа принимает имя папки и имя файла.
# Создает папку и создает в ней файл.
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-nd', '--name_dir')
parser.add_argument('-fn', '--file_name')
args = parser.parse_args()

if not os.path.isdir(args.name_dir):
    os.mkdir(args.name_dir)
file_path = os.path.join(args.name_dir, args.file_name)
file = open(file_path, 'w')
file.close()

if __name__ == '__main__':
    main()