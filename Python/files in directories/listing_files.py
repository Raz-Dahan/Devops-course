import sys
import os
import csv
import hashlib
#import multiprocessing


file_list = []

if len(sys.argv) == 1:
    sys.exit('You didn\'t named a directory, please add one and run the script again.')


def check_arg():
    DIR = sys.argv[1]
    while not (os.path.isdir(DIR)):
        print('The asked directory don\'t exists')
        DIR = input('Please correct: ')
    return DIR


def list_files(DIR):
    for root, dirs, files in os.walk(DIR):
        for file in files:
            file_list.append(os.path.join(root,file))
    for name in file_list:
        print(name)
    


def list_to_csv():
    files_info = open('files_info.csv', 'w', newline= '')
    writer = csv.writer(files_info)
    headers = ['number', 'file path' , 'md5 of the file']
    writer.writerow(headers)
    i = 1
    for file in file_list:
        reader = open(file,'rb').read()
        md5 = hashlib.md5(reader).hexdigest()
        row = [i, file, md5]
        writer.writerow(row)
        i += 1
    files_info.close()



def main():
    list_files(check_arg())
    list_to_csv()

if __name__ == "__main__":
    main()

