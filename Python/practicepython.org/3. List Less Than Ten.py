#print all the numbers that smaller than 5, one by one and in a new list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_a = []

for num in a:
    if num < 5:
        print(num)
        new_a.append(num)

print(new_a)

#print all the numbers that smallers than 15 in a new list, in one python line

A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
A = [i for i in A if i < 15]
print(A)

# return a new list of all the numbers that smaller than the user's input

NEW_A = []
NUM = int(input('Enter a number:'))

for num in a:
    if NUM > num:
        NEW_A.append(num)

print(NEW_A)