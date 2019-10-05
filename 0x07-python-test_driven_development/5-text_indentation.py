#!/usr/bin/python3
def text_indentation(text):

    new_list = []
    other_lista = []

    if type(text) is not str:
        raise TypeError("text must be a string")

    str1 = text.replace('.', '.\n\n')
    str2 = str1.replace('?', '?\n\n')
    str1 = str2.replace(':', ':\n\n')
    str1 = str1.strip()
    new_list = str1.split("\n")

    for i in new_list:
        other_lista.append(i.strip())

    print('\n'.join(other_lista))
