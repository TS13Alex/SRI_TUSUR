import pandas as pd
import csv
import os
from pathlib import Path
from pathlib import WindowsPath
from collections import defaultdict

def geting_file_paths():
    # Запрашиваем у пользователя путь к директории
    directory_path = input("Введите путь к директории с файлами: ")

    # Проверяем, является ли введенный путь абсолютной ссылкой
    if not os.path.isabs(directory_path):
        print("Введенный путь не является абсолютным.")
        return []
    else:
        # Получаем список всех файлов в директории
        csv_files = []
        for file in Path(directory_path).glob('**/*.csv'):
            if file.is_file():
                csv_files.append(str(file))
        return csv_files

file_paths = geting_file_paths()
if not file_paths:
    sys.exit("Нет CSV файлов для обработки.")

combined = pd.DataFrame()
for file in file_paths:
    try:
        data = pd.read_csv(file, encoding='cp1251')
        combined = pd.concat([combined, data])
    except PermissionError:
        print(f"Ошибка: Файл '{file}' уже открыт другим приложением. Пожалуйста, закройте его и попробуйте снова.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file}': {e}")

combined.to_csv('combined.csv', encoding='cp1251', index=False, sep=';')

def read_bom_csv(name_file: str):
    '''read csv file return list row'''
    readed_list = []
    name_and_family = []
    try:
        with name_file.open(encoding='cp1251', newline='') as vpcsvfile:
            rowreader = csv.reader(vpcsvfile, delimiter=';')
            next(rowreader)  # delete heading string
            next(rowreader)
            for row in rowreader:
                data_pe = [row[0], row[1], row[2], row[3]]
                readed_list.append(data_pe)
            name_and_family = [row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
    except PermissionError:
        print(f"Ошибка: Файл '{name_file}' уже открыт другим приложением. Пожалуйста, закройте его и попробуйте снова.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{name_file}': {e}")
    return readed_list, name_and_family

def Summation(name_file: str):
    dictionary = {}
    try:
        with name_file.open(encoding='cp1251', newline='') as f:
            rowreader = csv.reader(f, delimiter=';')
            next(rowreader)
            next(rowreader)
            count = 0
            for row in rowreader:
                for rows in rowreader:
                    if row[1] == rows[1]:
                        count += 1
                dictionary[row[1]] = count
                count = 0
    except PermissionError:
        print(f"Ошибка: Файл '{name_file}' уже открыт другим приложением. Пожалуйста, закройте его и попробуйте снова.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{name_file}': {e}")
    return dictionary

if __name__ == "__main__":
    p = WindowsPath(__file__)
    t = p.with_name('combined.csv')
    a, b = read_bom_csv(t)
    name_of_file = p.with_name('answer.csv')

    # Словарь для подсчета количества вхождений каждого уникального значения
    counts = defaultdict(int)

    # Открытие файла для чтения
    try:
        with open(t, newline='', encoding='cp1251') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';')

            # Пропуск заголовков
            next(csv_reader)
            next(csv_reader)
            
            # Проход по каждой строке файла
            for row in csv_reader:
                # Предполагается, что первый элемент каждой строки является ключом
                key = row[0]
                # Увеличение счетчика для данного ключа
                counts[key] += 1
    except PermissionError:
        print(f"Ошибка: Файл '{t}' уже открыт другим приложением. Пожалуйста, закройте его и попробуйте снова.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{t}': {e}")

    # Вывод результата
    for key, value in counts.items():
        print(f'{key}: {value}')
