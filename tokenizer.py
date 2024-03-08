import re
from pathlib import Path


def tokenizer(text):
    '''this method is used to convert a given text to tokens by changing all letters to lowercase letters
        and remove numbers. It also ignores words containing numbers'''
    with open('stopwordlist.txt', 'r') as swFile:
        stopwords = re.split(r'\s+', swFile.read())

    tokens = []
    for line in text:
        tokens += [token for token in re.split('[^a-zA-Z0-9]', line.lower()) if
                    not re.search('[0-9]', token) and token not in stopwords] # to perform tokenization on non-alphanumeric words, to remove empty words from the list, to ignore words containing numbers 
    return tokens