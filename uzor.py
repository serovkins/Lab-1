
first = 10
height = 9
width = first - 1
wvet_block = 0

gen = [int(x - 1) for x in range(first + 1, 2, -1)]

print(first * "\x1b[48;5;22;1m \x1b[0m" + (sum(gen) * 2 - first * 2 + 1) * " " + first * "\x1b[48;5;22;1m \x1b[0m")

for h in range(height):

    if width != 1:

        wvet_block += 1

        print(
            " " * sum(gen[0:wvet_block])
            + "\x1b[48;5;22;1m \x1b[0m" * gen[wvet_block]
            + (sum(gen) * 2 - (sum(gen[0:wvet_block + 1])) * 2 + 1) * " "
            + "\x1b[48;5;22;1m \x1b[0m" * gen[wvet_block]
            + " " * sum(gen[0:wvet_block])
        )

        width -= 1

    else:
 
        print((sum(gen)) * " " + "\x1b[48;5;22;1m \x1b[0m" + (sum(gen)) * " ")