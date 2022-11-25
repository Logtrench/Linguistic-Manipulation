def change_letter(letter: str, character: str, to: str) -> str:
    if letter == character:
        return to
    else:
        return ""


def is_char(char: list, check: str):
    for item in char:
        if item == check:
            return True
    return False


def capitalize(word):
    new_word = ""
    for i in range(len(word)):
        if i == 0:
            new_word += word[i].upper()
        else:
            new_word += word[i].lower()

    return new_word


def change_word(word):
    """
    """
    word = word.lower()
    new_word = ""
    for i in range(len(word)):
        char = word[i]
        word_length = len(new_word)

        # ŝ to sh
        new_word += change_letter("ŝ", char, "sh")
        new_word += change_letter("š", char, "sh")

        # ï to ee or i depending on where it is
        if i == 0:
            new_word += change_letter("ï", char, "i")
        elif i == len(word) - 2:
            new_word += change_letter("ï", char, "y")
        elif (i < len(word) - 2 and is_char(["a", "u", "ö", "è"], word[i + 1])):
            new_word += change_letter("ï", char, "iy")
        else:
            new_word += change_letter("ï", char, "ee")

        # è to e
        new_word += change_letter("è", char, "e")

        # ĉ, č to ch
        new_word += change_letter("ĉ", char, "ch")
        new_word += change_letter("č", char, "ch")

        # ö to œ
        new_word += change_letter("ö", char, "o")

        # Ð to dh
        new_word += change_letter("ð", char, "dh")

        # þ to th
        new_word += change_letter("þ", char, "th")

        # ŋ to n or ng, depending
        if (i <= len(word) - 2 and is_char(["a", "u", "ö", "è", "ï"], word[i + 1])) or i == len(word) - 2:
            new_word += change_letter("ŋ", char, "ng")
        else:
            new_word += change_letter("ŋ", char, "n")

        if len(new_word) == word_length:
            new_word += char

    new_word = capitalize(new_word)
    return new_word


def run():
    in_file = open("words_to_anglify.txt", "r", encoding="UTF-8")
    content = in_file.readlines()
    out_file = open("anglified.txt", "w+", encoding="UTF-8")
    for item in content:
        char = change_word(item)
        char = char.lower()
        out_file.write(char)

    print("done!")
