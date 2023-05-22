
a = [5, 10, 15, 20, 25]

def first_and_last(list):
    f_l_list = []
    f_l_list.append(list[0])
    f_l_list.append(list[-1])
    return f_l_list

print(first_and_last(a))