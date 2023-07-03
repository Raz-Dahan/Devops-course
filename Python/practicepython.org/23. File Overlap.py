file1 = open("C:\\Users\\razda\\OneDrive\\Documents\\ParcticePython.org\\23. File Overleap - happynumbers.txt", "r")
data1 = file1.read().split('\n')

file2 = open("C:\\Users\\razda\\OneDrive\\Documents\\ParcticePython.org\\23. File Overleap - primenumbers.txt", "r")
data2 = file2.read().split('\n')

def check_overleaps():
    overleaps = []
    for i in data1:
        if i in data2:
            overleaps.append(i)
    return overleaps


print(check_overleaps())