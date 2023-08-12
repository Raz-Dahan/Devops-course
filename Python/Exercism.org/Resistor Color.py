def color_code(color):
    return colors()[color]


def colors():
    color_dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
        }
    return color_dict



print(color_code('black'))