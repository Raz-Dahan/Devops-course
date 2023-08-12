

array = [3, 8, 12, 15, 20, 23, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]


def get_choice():
    choice = input('Choose a number to check if it\'s in the list and get it\'s position: ')
    while not choice.isnumeric():
        choice = input('The choice must be numeric, choose again: ')
    return int(choice)


def binary_search(choice, array):
    lst = list(array)
    while len(lst) > 0:
        mid = len(lst) // 2
        # print(lst, mid, lst[mid])                          """ remove comment to see steps """
        if choice < lst[mid]:
            lst = lst[:mid]
        elif choice > lst[mid]:
            lst = lst[mid+1:]
        elif choice == lst[mid]:
            print(f'Yes, {choice} is in the list at position {array.index(choice)}.')
            return
    print(f'The number {choice} is not in the list')


def main():
    binary_search(get_choice(), array)

if __name__ == "__main__":
    main()
