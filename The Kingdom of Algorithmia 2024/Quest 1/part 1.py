if __name__ == '__main__':
    file = open('input.txt')
    sequence = file.readline()
    sum1 = 0
    pmap = {'A': 0, 'B': 1, 'C': 3}

    while len(sequence):
        character = sequence[0]
        sum1 += pmap[character]
        sequence = sequence[1:]

    print(sum1)