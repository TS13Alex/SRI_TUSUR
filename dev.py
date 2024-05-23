import pandas as pd
import csv
import os
from pathlib import Path
from pathlib import WindowsPath
def geting_file_paths():
    # Запрашиваем у пользователя путь к директории
    directory_path = input("Введите путь к директории с файлами: ")

    # Проверяем, является ли введенный путь абсолютной ссылкой
    if not os.path.isabs(directory_path):
        print("Введенный путь не является абсолютным.")
    else:
        # Получаем список всех файлов в директории
        csv_files = []
        for file in Path(directory_path).glob('**/*'):
            if file.is_file() and file.suffix == '.csv':
                csv_files.append(str(file))
    return (csv_files)
file_paths = geting_file_paths()
with open( "combined.csv", "w", encoding='cp1251') as data:   
    combined = pd.DataFrame()
    for file in file_paths:
        data = pd.read_csv(file, encoding= 'cp1251',)
        combined = pd.concat([combined, data])
    combined.to_csv('combined.csv', encoding= 'cp1251',index= False, sep = ';')

def read_bom_csv(name_file: str):
    '''read csv file return list row'''
    with name_file.open (encoding='cp1251', newline='') as vpcsvfile:
        rowreader = csv.reader(vpcsvfile, delimiter=';')
        next(rowreader) # delete heading string
        next(rowreader)
        readed_list = []
        for row in rowreader:
            data_pe = [row[0], row[1], row[2], row[3]]
            readed_list.append(data_pe)
        name_and_family = [row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
    return (readed_list, name_and_family)

def Summation(name_file: str):
    with name_file.open(encoding='cp1251', newline='') as f:
        rowreader = csv.reader(f, delimiter=';' )
        next(rowreader)
        next(rowreader)
        dictionary = {}
        count = 0
        for row in rowreader:
            for rows in rowreader:
                if row[1] == rows[1]:
                    count += 1
            dictionary = {row:count}
            count = 0
        return dictionary

if __name__ == "__main__":
    p = WindowsPath(__file__)
    t = p.with_name('combined.csv')
    a, b = read_bom_csv(t)
    name_of_file = p.with_name('answer.csv')
    dict_of_summ = Summation(name_of_file)
    print (dict_of_summ)

    
    
    '''with open( "answer.csv", "r+", encoding='cp1251') as data:
        writer = csv.writer(data)
        for line in a :
            writer.writerow(line)
        with open("summation.csv", "w") as f:
            writer = csv.writer(f)
            count = 0
            for i in data:
                for j in data:
                    if len(i)>=3:
                        if (i[1] == j[1]):
                            count += 1
                        if (i not in(f)):
                            i[2] = count
                        writer.writerow(i)
        '''              