if __name__ == '__main__':
    potion_needed = {'A': 0, 'B': 1, 'C': 3}

    file = open('input.txt')
    sequence = file.readline()
    sum = 0

    for character in sequence:
        potions = potion_needed[character]
        sum += potions

    print(sum)
