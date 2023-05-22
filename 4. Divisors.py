
DIV = int(input('Enter a number:'))
divisors = []

for num in range(2, DIV):
    if DIV % num == 0:
        divisors.append(num)

print(divisors)