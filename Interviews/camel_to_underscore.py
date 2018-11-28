def read_input():
    return [input() for i in range(int(input()))]


def get_next_word(variable, index):
    length = len(variable)
    if index + 1 == length:
        return index+1, variable[index].lower()
    # There are more letters
    cur_letter = variable[index]
    next_letter = variable[index+1]
    index_end = index + 1
    if cur_letter.isupper() and next_letter.isupper():
        # AA
        while index_end < length and variable[index_end].isupper():
            index_end += 1
        index_end = index_end - 1 if index_end > len(variable) else index_end
        return index_end, variable[index:index_end]
    elif next_letter.islower():
        # Aa or aa
        while index_end < length and variable[index_end].islower():
            index_end += 1
        return index_end, variable[index:index_end]
    else:
        # aA
        return index+1, variable[index]


def camel_to_underscore(variable):
    index = 0
    underscore = ""
    while index < len(variable):
        (index, word) = get_next_word(variable, index)
        underscore += '_' + word.lower()
    print(underscore.strip('_'))


[camel_to_underscore(variable) for variable in read_input()]
