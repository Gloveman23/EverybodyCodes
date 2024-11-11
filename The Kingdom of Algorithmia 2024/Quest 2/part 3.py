if __name__ == '__main__':
    file = open('input.txt')

    lines = file.readlines()

    words = lines[0]
    words = words[6:-1]
    words = words.split(',')

    max_len = max(len(w) for w in words)

    runes = lines[2:]

    total = 0

    for i in range(len(runes)):
        if runes[i][-1] == '\n':
            runes[i] = runes[i][:-1]
        line = runes[i]
        runes[i] = line[-max_len:] + line + line[:max_len]

    trackers = []

    for rune in runes:
        tracker = [False for char in rune]
        for i in range(len(rune)):
            for word in words:
                if len(word) > len(rune) - i:
                    continue
                f = True
                b = True
                for j in range(len(word)):
                    if word[j] != rune[j+i]:
                        f = False
                    if word[j] != rune[i + len(word) - j - 1]:
                        b = False
                if f or b:
                    for k in range(i, i + len(word)):
                        tracker[k] = True
        trackers += [tracker]

    for i in range(len(runes)):
        runes[i] = runes[i][max_len:-max_len]
        trackers[i] = trackers[i][max_len:-max_len]

    for R in range(len(runes[0])):
        rune = [runes[j][R] for j in range(len(runes))]
        rune = "".join(rune)
        for i in range(len(rune)):
            for word in words:
                if len(word) > len(rune) - i:
                    continue
                f = True
                b = True
                for j in range(len(word)):
                    if word[j] != rune[j + i]:
                        f = False
                    if word[j] != rune[i + len(word) - j - 1]:
                        b = False
                if f or b:
                    for k in range(i, i + len(word)):
                        trackers[k][R] = True

    rune1 = runes
    for i in range(len(rune1)):
        tracker = trackers[i]
        for j in range(len(tracker)):
            if tracker[j]:
                rune1[i] = rune1[i][:j] + runes[i][j].lower() + rune1[i][j+1:]
        rune1[i] = rune1[i].swapcase()
        print(rune1[i])

    total = sum(sum(1 for b in tracker if b) for tracker in trackers)

    print(f'Total: {total}')
