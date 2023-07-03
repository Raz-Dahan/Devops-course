#!/usr/bin/python3
import sys
import json

string = sys.argv[1]
DICT = {}

for x in string:
    DICT[x] = string.count(x)

print(DICT)


dictionar = open("dictionar.json", "w")
json.dump(DICT, dictionar)