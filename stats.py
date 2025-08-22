def word_count(text):
    return len(text.split())

def character_count(string):
    num_character = {}
    for char in string:
        lowered = char.lower()
        if lowered in num_character:
            num_character[lowered] += 1
        else:
            num_character[lowered] = 1
    return num_character

def sort_on(items):
    return items['num']

def list_sort(list):
    new_list = []
    for l in list:
        new_list.append({'char': l, 'num': list[l]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list