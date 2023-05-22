
c = [1, 1, 2, 3, 3, 3]

def remove_duplicates(list):
    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)
    print(new_list)

remove_duplicates(c)

C = list(set(c))

print(C)