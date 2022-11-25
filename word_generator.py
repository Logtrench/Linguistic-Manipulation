# used in generating new word
import random

# used to see how efficient code is
import datetime

# vowel code
vowels = ["a", "u", "o", "ï", "e", "i", "é",
          "è", "ä", "ü", "à", "á", "ò", "ö", "è", "é"]


def break_word(word: str) -> list:
    """
    """
    # syllable will be returned in the end
    syllables = []
    # vowel location will simply state where there is a vowel
    vowel_loc = []
    # split position will be the location that the word will split. It will split from the (inclusive) position to the (exclusive) next.
    split_pos = []

    # find the vowels.
    for i in range(0, len(word)):
        if word[i] in vowels:
            vowel_loc += [i]

    # debugging, uncomment if needed
    #print("vowel locations", vowel_loc)

    # this loop will make the split position at every half-way point(rounded up) between vowels
    for i in range(len(vowel_loc) - 1):
        split_pos += [round((vowel_loc[i] + vowel_loc[i + 1] + 1) / 2)]

    # debugging, uncomment if needed
    #print("split positions", split_pos)

    # perform special case for short words
    if len(split_pos) == 1:
        syllables += [word[0:split_pos[0]]]
        syllables += [word[split_pos[0]:]]

    # perform special case for words with only one vowel
    if len(split_pos) == 0:
        syllables += [word]

    # if longer word, do this;
    else:

        # this loop will actually split the word into syllables
        for i in range(len(split_pos) - 1):

            # add the beginning of the word
            if i == 0:
                # from word[0] to the first split position
                syllables += [word[0:split_pos[i]]]

            # from split position to the next split position
            syllables += [word[split_pos[i]:split_pos[i + 1]]]

            # add the end of the word as well
            if i == len(split_pos) - 2:
                # from the last split location to the end of the word
                syllables += [word[split_pos[i + 1]:len(word)]]

    # return the syllable
    return syllables


def break_syl(syllable: str) -> tuple:
    # positioning
    pos = -1
    pos2 = -1
    for i in range(len(syllable)):
        if syllable[i] in vowels:
            if pos == -1:
                pos = i
            else:
                pos2 = i

    onset = syllable[0:pos]
    if len(syllable) == 0:
        return ("", "", "")
    elif pos2 != -1:
        nucleus = syllable[pos:(pos2 + 1)]
        coda = syllable[pos2 + 1:len(syllable)]
    else:
        nucleus = syllable[pos]
        coda = syllable[pos + 1:len(syllable)]

    return (onset, nucleus, coda)


def get_words(source: str) -> list:
    in_file = open(source, "r", encoding="UTF-8")
    content = in_file.readlines()

    words = []
    for item in content:
        item = item.rstrip()
        item = item.strip()
        item = item.lower()
        item = item.replace("\n", "")
        words += [item]

    in_file.close()

    return words


def analyze(words: list) -> tuple:
    # growing lists containing the samples
    onset_list = []
    nucleus_list = []
    coda_list = []

    for word in words:
        syllables = break_word(word)
        for syl in syllables:
            (onset, nucleus, coda) = break_syl(syl)
            onset_list += [onset]
            nucleus_list += [nucleus]
            coda_list += [coda]
    return(onset_list, nucleus_list, coda_list)


def create(lists: tuple) -> str:
    onsets, nuclei, codas = lists

    print("One Syllable Words:")
    for i in range(5):
        print(onsets[random.randint(0, len(onsets) - 1)], end="")
        print(nuclei[random.randint(0, len(nuclei) - 1)], end="")
        print(codas[random.randint(0, len(codas) - 1)])

    print("\nTwo Syllable Words:")

    for i in range(5):
        print(onsets[random.randint(0, len(onsets) - 1)], end="")
        print(nuclei[random.randint(0, len(nuclei) - 1)], end="")
        print(codas[random.randint(0, len(codas) - 1)], end="")

        print(onsets[random.randint(0, len(onsets) - 1)], end="")
        print(nuclei[random.randint(0, len(nuclei) - 1)], end="")
        print(codas[random.randint(0, len(codas) - 1)])

    print("\nThree Syllable Words:")

    for i in range(5):
        print(onsets[random.randint(0, len(onsets) - 1)], end="")
        print(nuclei[random.randint(0, len(nuclei) - 1)], end="")
        print(codas[random.randint(0, len(codas) - 1)], end="")

        print(onsets[random.randint(0, len(onsets) - 1)], end="")
        print(nuclei[random.randint(0, len(nuclei) - 1)], end="")
        print(codas[random.randint(0, len(codas) - 1)], end="")

        print(onsets[random.randint(0, len(onsets) - 1)], end="")
        print(nuclei[random.randint(0, len(nuclei) - 1)], end="")
        print(codas[random.randint(0, len(codas) - 1)])


def auto_make(source: str) -> str:
    start = datetime.datetime.now()
    start = start.microsecond

    create(analyze(get_words(source)))

    end = datetime.datetime.now()
    end = end.microsecond

    print(end - start)



