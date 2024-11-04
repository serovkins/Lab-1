FIRST = 10
HEIGHT = 9
WIDTH = FIRST - 1
WVET_BLOCK = 0

GEN = [int(x - 1) for x in range(FIRST + 1, 2, -1)]

print(FIRST * "\x1b[48;5;22;1m \x1b[0m" + (sum(GEN) * 2 - FIRST * 2 + 1) * " " +
      FIRST * "\x1b[48;5;22;1m \x1b[0m")

for h in range(HEIGHT):
    if WIDTH != 1:
        WVET_BLOCK += 1
        print(
            " " * sum(GEN[0:WVET_BLOCK])
            + "\x1b[48;5;22;1m \x1b[0m" * GEN[WVET_BLOCK]
            + (sum(GEN) * 2 - (sum(GEN[0:WVET_BLOCK + 1])) * 2 + 1) * " "
            + "\x1b[48;5;22;1m \x1b[0m" * GEN[WVET_BLOCK]
            + " " * sum(GEN[0:WVET_BLOCK])
        )
        WIDTH -= 1
    else:
        print((sum(GEN)) * " " + "\x1b[48;5;22;1m \x1b[0m" + (sum(GEN)) * " ")