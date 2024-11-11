if __name__ == '__main__':
    potion_needed = {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x':0}

    file = open('input.txt')
    sequence = file.readline()

    if len(sequence) % 2 != 0:
        sequence += 'x'

    sum = 0

    while len(sequence) > 0:
        character1 = sequence[0]
        character2 = sequence[1]
        potions = potion_needed[character1] + potion_needed[character2]
        if character1 != 'x' and character2 != 'x':
            potions += 2
        sum += potions
        sequence = sequence[2:]
    print(sum)
