if __name__ == '__main__':
    file = open('input.txt')

    lines = file.readlines()

    words = lines[0]
    words = words[6:-1]
    words = words.split(',')

    max_len = max(len(w) for w in words)

    runes = lines[2:]

    total = 0

    for rune in runes:
        rune1 = rune
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
        for i in range(len(rune) - 1):
            if tracker[i]:
                rune1 = rune1[:i] + (rune[i]).lower() + rune1[i+1:]
        rune1 = rune1[:-1]
        found = sum(1 for x in tracker if x)
        total += found
        print(rune1.swapcase() + f' ({found})')


    print(f'Total: {total}')
