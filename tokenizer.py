import re


def tokenizer(doc):
    

    tokens = re.findall(r'\b\w+\b', doc.lower()) 

    tokens = [toekn for toekn in tokens if not any(char.isdigit() for char in toekn)] 

    tokens = list(filter(None, tokens)) 

    return tokens


def tokenizer(text):
    '''this method is used to convert a given text to tokens by changing all letters to lowercase letters
        and remove numbers. It also ignores words containing numbers'''
    tokens = []
    for line in text:
        tokens += [token for token in re.split('[^a-zA-Z0-9]', line.lower()) if
                    not re.search('[0-9]', token)] # to perform tokenization on non-alphanumeric words, to remove empty words from the list, to ignore words containing numbers 
    return tokens