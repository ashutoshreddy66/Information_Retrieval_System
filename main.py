import os
from pathlib import Path
from WordDictionary import WordDictionary
from FileDictionary import FileDictionary
from tokenizer import tokenizer
from DocParser import DocParser


def parser_output(data, mode):
    parser_file = "parser_output.txt"
    try:
        filePath = os.path.join(Path(__file__).parent.resolve(), parser_file)
        with open(filePath, mode) as parser_output:
            for key in sorted(data.keys()):
                parser_output.write(f"{key}\t{data[key]}\n")
        print("Parser output: Writing data COmpleted!")
    except:
        print("Parser output: error while uploading data")

path = "./ft911/"

folder = os.listdir(path=path)

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

parser_output(WordDict.fetch_d(), 'w')#once all the word data is feteched, we write the data to the output file using the 'w' mode
parser_output(FileDict.getAllFiles(), 'a')#once all the filenames are feteched, we append the data to the output file using the 'a' mode
