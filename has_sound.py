from Anglicize import capitalize


"""
This program takes words from a list and then lists every word that has the desired sounds, as well as the meaning of said word

"""


def write_comma(source1: str, source2: str, output):
    word_file = open(source1, "r", encoding="UTF-8")
    words = word_file.readlines()
    print(words)

    meaning_file = open(source2, "r")
    meanings = meaning_file.readlines()
    print(meanings)

    output_file = open(output, "w+", encoding="UTF-8")

    counter = 0
    meaning_list = []
    for item in meanings:
        print(item)
        meaning_list += [str(item).rstrip()]
        counter += 1

    word_list = []
    for item in words:
        word_list += [str(item)]

    for i in range(counter):
        output_file.write(str(meaning_list[i]) + ", " + str(word_list[i]))


def has_sound(sound: str) -> list:
    word_file = open("words_and_meaning.txt", "r", encoding="UTF-8")

    lines = word_file.readlines()

    has_it = []
    for item in lines:
        item = item.lower()
        temp_sound = item.split(",")
        phone = temp_sound[1]
        if sound in phone:
            has_it += [item.rstrip()]

    for item in has_it:
        print(capitalize(item))

    return has_it
