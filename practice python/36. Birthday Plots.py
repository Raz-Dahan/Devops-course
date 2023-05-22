from json import load, dump
from collections import Counter
from bokeh.plotting import figure, show

Path = "C:\\Users\\razda\\OneDrive\\Documents\\ParcticePython.org\\34. Birthday Json - file.json"
file = open(Path, 'r+')
data = load(file)



def choose_action():
    print('Would you like to do? \n<know> a birthday \n<add> a birthday \n<show> all birthdays in a plot')
    answer = input().lower()
    while (answer != 'know') and (answer != 'add') and (answer != 'show'):
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
        dump(data, f)
    print('Player details have been added!')

def months_plot():
    months_list = []
    months_dict = {}
    for key in data:
        value = data[key]
        month = str(value).split(' ')[0]
        months_list.append(month)
    months_dict = dict(Counter(months_list))
    x_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    plot = figure(title="How many players was born per months", x_axis_label="Months", y_axis_label="Players", x_range=x_months)
    x = list(months_dict.keys())
    y = list(months_dict.values())
    plot.vbar(x=x, top=y, legend_label="Amount", width=0.5, bottom=0, color="blue")
    show(plot)




def main():
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for key in data:
        print('· ' + key)
    answer = choose_action()
    if answer == 'know':
        give_birthday()
    elif answer == 'add':
        add_birthday()
    elif answer == 'show':
        months_plot()
    file.close()
    

if __name__ == "__main__":
    main()