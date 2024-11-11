if __name__ == '__main__':
    file = open('input.txt')
    words = file.readline()
    words = words[6:-1]
    words = words.split(',')

    file.readline()

    runes = file.readline()

    max_len = max(len(w) for w in words)

    while len(runes) % max_len != 0:
        runes += '?'

    total = 0

    next_test = runes[:max_len]

    while len(next_test) >= max_len:
        for word in words:
            match = True
            for i in range(len(word)):
                if word[i] != next_test[i]:
                    match = False
            if match:
                total += 1

        runes = runes[1:]
        next_test = runes[:max_len]

    print(total)