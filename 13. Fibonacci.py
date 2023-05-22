
def fibonacci():
    times = int(input('How many fibonacci numbers do you want:'))
    while not times > 0:
        times = int(input('It must be greater than 0:'))
    return execute(times)

def execute(times):
    fibo_list = [1, 1]
    if times == 1:
        return [1]
    elif times == 2:
        return [1, 1]
    elif times > 2:
        for i in range(times - 2):
            fibo = fibo_list[i] + fibo_list[(i+1)]
            fibo_list.append(fibo)
        return fibo_list


    

print(fibonacci())