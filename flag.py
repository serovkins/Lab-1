
red = '\x1b[48;5;196m'
yellow = '\x1b[48;5;220m'
green = '\x1b[48;5;22m'
stop = '\x1b[0m'



def line(color):
    line  = ' '*37
    print(color, line, stop, end = '')

def flag():
    for i in range(3):
        line(yellow)
        print()
    for i in range(3):
        line(green)
        print()
    for i in range(3):
        line(red)
        print()
flag()