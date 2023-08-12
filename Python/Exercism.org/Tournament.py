
with open("C:\\Users\\razda\\OneDrive\\Documents\\Exercism.org\\Python\\Tournament_file.txt") as f:
    data = f.readlines()

games = [line.rstrip().split(';') for line in data]

def tally():
    teams = list(set([game[i] for game in games for i in range(2)]))
    max_length = max(len(team) for team in teams)
    print("{:<{}} |".format('Teams', max_length))
    for team in teams:
        print("{:<{}} |".format(team, max_length))
    



tally()











f.close()
