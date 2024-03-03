import re
import os

def tokenizer(doc):
    '''this method is used to convert a given text to tokens by changing all letters to lowercase letters
        and remove numbers. It also ignores words containing numbers'''
    doc = re.sub(r'\d+', '', doc)
    doc = doc.lower()

    tokens = re.split(r'[^a-zA-Z\']+', doc) # to perform tokenization on non-alphanumeric words

    tokens = [toekn for toekn in tokens if not any(char.isdigit() for char in toekn)] # to ignore words containing numbers

    tokens = list(filter(None, tokens)) #to remove empty words from the list

    return tokens



from nltk.stem import PorterStemmer

class WordDictionary:
    #first we define a constructor to initialize our variables
    def __init__(self):
        self.wordIDs = {} #dict for all word ids
        self.currWordId = 1 #start with id 1 for words
        self.stemmer = PorterStemmer() #initalize stemmer obj

    def appendWord(self, word):
        stemWord = self.stemmer.stem(word) #setup the stem word
        if(stemWord not in self.wordIDs): #check if the dict contains the word
            self.wordIDs[stemWord] = self.currWordId #if the word is not present we add the word to the dict along with the id
            self.currWordId += 1 #increment the id for the next word

    def getWordId(self, word):
        stemWord = self.stemmer.stem(word)
        return self.wordIDs.get(stemWord, None)
    


class FileDictionary:
    #similar to WordDictionary we do the initialize step
    def __init__(self, path):
        self.fileIDs = {} #dict for all file ids
        self.currFileId = 1#start with id 1 for files
        self.folder = path#set a foldder ref with the given path

    def getFileId(self, file):
        return self.fileIDs.get(file, None)

    def appendFiles(self):
        Files = os.listdir(self.folder) #setup all the files from the folder 
        for File in Files:
            if(File.startswith("ft911_")): #looping over all files to see if it starts with ft911
                self.fileIDs[File] = self.currFileId #if condiction is satisified we add it to our dict along with an ID
                self.currFileId += 1 #increment the id for the next word
    
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

    for docId, text in complete_data:
        line = f"{docId}\t{FileDict.getFileId(docId)}\n"
        if(line not in opSet):
            opSet.add(line)

        tokens = tokenizer(text)
        for token in tokens:
            WordDict.appendWord(token)
            outputLine = f"{token}\t{WordDict.getWordId(token)}\n"
            if(outputLine not in opSet):
                opSet.add(outputLine)

    
    opList = list(opSet)
    # opList.sort()
    #writing data into the parser_output file
    for i in opList:
        parser_output.write(i)
        print(i)