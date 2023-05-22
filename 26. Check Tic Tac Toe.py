
def check_win(game):
    list1 = game[0]
    list2 = game[1]
    list3 = game[2]
    for list in game:
        for i in range(len(list)):
            if list1[i] == list2[i] == list3[i] and list1[i] != 0:
                return True
            if len(list(dict.fromkeys(list1))) == 1 and list1[0] != 0 or len(list(dict.fromkeys(list2))) == 1 and list2[0] != 0 or len(list(dict.fromkeys(list3))) == 1 and list3[0] != 0:
                return True
            elif list1[0] == list2[1] == list3[2] and list1[1] != 0 or list1[2] == list2[1] == list3[0] and list1[1] != 0:
                return True
        return False
        

print(check_win([[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]))
