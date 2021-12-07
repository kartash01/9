def sort_sentence(sentence):
    import operator
    fi = sentence.split(' ')
    ru = {i : len(i) for i in fi}
    sorted_tu = sorted(ru.items(), key=operator.itemgetter(1))
    string = ''
    for key, i in sorted_tu:
        string += key + ' '
    return string