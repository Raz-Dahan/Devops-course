

names_file = open("C:\\Users\\razda\\OneDrive\\Documents\\ParcticePython.org\\22. Read From File - names.txt", "rt")
data = names_file.read().split('\n')
results = []

for name in data:
    times = data.count(name)
    SUM = name + ' = ' + str(times)
    if SUM not in results:
        results.append(SUM)

names_file.close()

print(results)
