import sys

WORD = sys.argv[1]
PATH = sys.argv[2]

text_file = open('test.txt', 'r', newline= '').readlines()

for line in text_file:
    if 'test' in line:
        print(line)

TEXT_FILE = open(PATH, 'r', newline= '').readlines()

for line in TEXT_FILE:
    if WORD in line:
        print(line)
