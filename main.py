import os
from pathlib import Path
from WordDictionary import WordDictionary
from FileDictionary import FileDictionary
from tokenizer import tokenizer
from DocParser import DocParser
from datetime import datetime

print("Running code at:", datetime.now())

path = "./ft911/"
folder = os.listdir(path=path)

parser_file = "parser_output.txt"
w = 'w'
a = 'a'

def parser_output(data, mode):    
    try:#exception handling
        filePath = os.path.join(Path(__file__).parent.resolve(), parser_file)#created a file if it doesn't already exist to write output
        with open(filePath, mode) as parser_output:
            for key in sorted(data.keys()):#iterates through all docnos and stemmed words
                parser_output.write(f"{key}\t{data[key]}\n")#appeninf the DOCNO: DOCID and Word : WOrdID to the parser_output file
        print("Parser output- Success: Writing data COmpleted!")
    except:#shows error message in case of failure
        print("Parser output- Failure: error while uploading data")


#then we initialize our custom dictionaries
WordDict = WordDictionary()
FileDict = FileDictionary(path)

#looping over all the files in the folder mentioned above and and adding them to complete data
for file in folder:
    docs = DocParser.fetchDocs(file)
    for docno, data in docs.items():
        FileDict.appendFiles(docno)
        tokens = tokenizer(data)
        for token in tokens:
            WordDict.appendWord(token)

parser_output(WordDict.fetch_d(), w)#once all the word data is feteched, we write the data to the output file using the 'w' mode
parser_output(FileDict.getAllFiles(), a)#once all the filenames are feteched, we append the data to the output file using the 'a' mode
