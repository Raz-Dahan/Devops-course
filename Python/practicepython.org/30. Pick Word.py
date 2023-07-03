from random import choice

file = open("C:\\Users\\razda\\OneDrive\\Documents\\ParcticePython.org\\30. Pick Word - sowpods.txt", "r")
data = file.read().split('\n')

print(choice(data))