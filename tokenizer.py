import re


def tokenizer(doc):
    '''this method is used to convert a given text to tokens by changing all letters to lowercase letters
        and remove numbers. It also ignores words containing numbers'''
    doc = re.sub(r'\d+', '', doc)
    doc = doc.lower()

    tokens = re.split(r'[^a-zA-Z\']+', doc) # to perform tokenization on non-alphanumeric words

    tokens = [toekn for toekn in tokens if not any(char.isdigit() for char in toekn)] # to ignore words containing numbers

    tokens = list(filter(None, tokens)) #to remove empty words from the list

    return tokens