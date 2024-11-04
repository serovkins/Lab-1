RED = '\x1b[48;5;196m'
YELLOW = '\x1b[48;5;220m'
GREEN = '\x1b[48;5;22m'
STOP = '\x1b[0m'


def line(color):
    line = ' ' * 37
    print(color, line, STOP, end='')


def flag():
    for _ in range(3):
        line(YELLOW)
        print()
    for _ in range(3):
        line(GREEN)
        print()
    for _ in range(3):
        line(RED)
        print()


flag()