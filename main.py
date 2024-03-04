import re
import os
from WordDictionary import WordDictionary
from FileDictionary import FileDictionary
from docnos import extract_docno
from tokenizer import tokenizer



complete_data = []
path = "./ft911/"

folder = os.listdir(path=path)

#looping over all the files in the folder mentioned above and and adding them to complete_data
for file in folder:
    with open(os.path.join(path, file), "r") as File:
        file_data = File.read()
        complete_data.append((file, file_data))

#then we initialize our custom dictionaries
WordDict = WordDictionary()
FileDict = FileDictionary(path)

FileDict.appendFiles() #appending files to file dict

#Performing data preprocessing and providing the final output

with open("parser_output.txt", "w") as parser_output:
    opSet = set() #for holding non-redundant values
    all_file_IDs = FileDict.getAllFiles()
    for docId, text in complete_data:
        for docno, fileID in all_file_IDs.items():
            line = f"{docno}\t{fileID}\n"
            if line not in opSet:
                opSet.add(line)

        tokens = tokenizer(text)
        for token in tokens:
            WordDict.appendWord(token)
            outputLine = f"{token}\t{WordDict.getWordId(token)}\n"
            if(outputLine not in opSet):
                opSet.add(outputLine)

    
    opList = list(opSet)
    opList.sort()
    #writing data into the parser_output file
    for i in opList:
        parser_output.write(i)
        # print(i)