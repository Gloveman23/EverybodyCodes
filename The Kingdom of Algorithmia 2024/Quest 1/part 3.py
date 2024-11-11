if __name__ == '__main__':
    file = open('input.txt')
    sequence = file.readline()
    sum1 = 0
    pmap = {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0}
    xmap = {3:2, 2:1, 1:0, 0:0}

    while len(sequence):
        characters = sequence[0:3]
        num_e = sum(1 for x in characters if x != 'x')
        sum1 += sum(pmap[character] + xmap[num_e] for character in characters if character != 'x')
        sequence = sequence[3:]
        print(characters)

    print(sum1)