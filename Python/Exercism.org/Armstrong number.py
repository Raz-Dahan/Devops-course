def is_armstrong_number(number):
    NUMBER = str(number)
    result = 0
    for digit in NUMBER:
        digit_sum = int(digit) ** len(NUMBER)
        result = result + digit_sum
    if result != number:
        return False
    else:
        return True