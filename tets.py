with open('test.txt', 'r') as file:
    while True:
        now = file.readline()
        if now == '':
            break
        print(now, end='')
