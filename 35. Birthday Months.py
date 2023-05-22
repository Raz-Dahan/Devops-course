import json
from collections import Counter

Path = "C:\\Users\\razda\\OneDrive\\Documents\\ParcticePython.org\\34. Birthday Json - file.json"
file = open(Path, 'r+')
data = json.load(file)
months_list = []

def count_months():
    for key in data:
        value = data[key]
        month = str(value).split(' ')[0]
        months_list.append(month)
    months_dict = dict(Counter(months_list))
    print(months_dict)


def main():
    count_months()
    file.close()
    

if __name__ == "__main__":
    main()