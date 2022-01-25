def t(file_name):
    dct = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        text = ''.join(el.lower() for el in file.read() if el.isalpha())
        for el in text:
            if el not in dct.keys():
                dct[el] = 1
            else:
                dct[el] += 1
    return dct
result = t('text.txt')
print(result)


