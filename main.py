import os
import time
from pathlib import Path
from WordDictionary import WordDictionary
from FileDictionary import FileDictionary
from tokenizer import tokenizer
from DocParser import TextParser
from datetime import datetime
from indexer import Indexer
import nltk
from nltk.stem import PorterStemmer

# nltk.download('punkt')


print("Running code at:", datetime.now())

path = "./ft911/"
folder = os.listdir(path=path)

parser_file = "parser_output.txt"
forward_index_file = "forward_index.txt"
inverted_index_file = "inverted_index.txt"
w = 'w'
a = 'a'

def parser_output(fileName, data, mode):    
    try:#exception handling
        filePath = os.path.join(Path(__file__).parent.resolve(), fileName)#created a file if it doesn't already exist to write output
        with open(filePath, mode) as parser_output:
            for key in data.keys():#iterates through all docnos and stemmed words
                parser_output.write(f"{key}\t{data[key]}\n")#appeninf the DOCNO: DOCID and Word : WOrdID to the parser_output file
        print("Parser output- Success: Writing data COmpleted!")
    except:#shows error message in case of failure
        print("Parser output- Failure: error while uploading data")


#then we initialize our custom dictionaries
WordDict = WordDictionary()
FileDict = FileDictionary(path)


def get_stem_words(forward_words):
    stemmer = PorterStemmer() 
    stemmed_words = []
    for word in forward_words:
        stemword = stemmer.stem(word)
        if stemword == "":
            pass
        elif stemword not in stemmed_words:
            stemmed_words.append(stemword)
    return stemmed_words

forwardIndex = {}
forward_tokens = []
#looping over all the files in the folder mentioned above and and adding them to complete data
for file in folder:
    docs = TextParser.fetchDocs(file)
    for docno, data in docs.items():
        FileDict.appendFiles(docno)
        tokens = tokenizer(data)
        for token in tokens:
            WordDict.appendWord(token)
        stemmed_words = get_stem_words(tokens)
        forwardIndex[docno] = stemmed_words

start = time.time()
new_forwardIndex = Indexer.create_forward_index(forwardIndex)
Indexer.write_forward_index(new_forwardIndex, forward_index_file)

inverted_index = Indexer.create_inverted_index(new_forwardIndex)
Indexer.write_inverted_index(inverted_index, inverted_index_file)

print("Time taken to generate indexes: " + str(round(time.time() - start)) + " seconds")
# print("The size of inverted index is: " + str(len(WordDict.get_dict().keys())))

parser_output(parser_file, WordDict.fetch_d(), w)#once all the word data is feteched, we write the data to the output file using the 'w' mode
parser_output(parser_file, FileDict.getAllFiles(), a)#once all the filenames are feteched, we append the data to the output file using the 'a' mode
