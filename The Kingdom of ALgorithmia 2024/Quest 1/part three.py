if __name__ == '__main__':
    potion_needed = {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0}

    file = open('input.txt')
    sequence = file.readline()

    while len(sequence) % 3 != 0:
        sequence += 'x'


    sum1 = 0

    while len(sequence) > 0:
        characters = sequence[0:3]
        num_x = sum(1 for x in characters if x == 'x')
        extras = 0
        potions = 0
        if num_x == 1:
            extras = 1
        if num_x == 0:
            extras = 2
        for character in characters:
            if character != 'x':
                potions += potion_needed[character] + extras
        sequence = sequence[3:]
        sum1 += potions
    print(sum1)