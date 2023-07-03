import datetime

NAME = input('Enter you name:')
AGE = int(input('Enter your age:'))

today = datetime.date.today()
YEAR = str(today.year - AGE + 100)

print(NAME + ' will be 100 years old in ' + YEAR)