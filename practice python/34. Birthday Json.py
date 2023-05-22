import json

Path = "C:\\Users\\razda\\OneDrive\\Documents\\ParcticePython.org\\34. Birthday Json - file.json"
file = open(Path, 'r+')
data = json.load(file)


def choose_action():
    print('Would you like to <know> a birthday or <add> a birthday?')
    answer = input().lower()
    while (answer != 'know') and (answer != 'add'):
        print('Please type <know> or <add>:')
        answer = input().lower()
    return answer    

def give_birthday():
    print('Who\'s birthday do you want to look up?')
    player = input()
    print(f'{player}\'s birthday is {data[player]}')

def add_birthday():
    print('What\'s the player\'s name?')
    key = input()
    print('What\'s the player\'s birthday?')
    value = input()
    new_data = {key:value}
    data.update(new_data)
    with open(Path, 'w') as f:
        json.dump(data, f)
    print('Player details have been added!')



def main():
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for key in data:
        print(key)
    answer = choose_action()
    if answer == 'know':
        give_birthday()
    elif answer == 'add':
        add_birthday()
    file.close()
    

if __name__ == "__main__":
    main()