n = 0
h = 9

for i in range(h):
    print(' ' * (h - i - 1), end='')  
    print('\x1b[48;5;22;1m \x1b[0m', end='') 
    print()
    n += 1