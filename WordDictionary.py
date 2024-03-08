import nltk
from nltk.stem import PorterStemmer

# nltk.download('punkt')

all_words = []

class WordDictionary:
    #first we define a constructor to initialize our variables
    def __init__(self):
        self.wordIDs = {} #dict for all word ids
        self.currWordId = 1 #start with id 1 for words
        self.stemmer = PorterStemmer() #initalize stemmer obj

    def appendWord(self, word):
        stemWord = self.stemmer.stem(word) #setup the stem word
        if stemWord == "":
            pass
        elif stemWord not in self.wordIDs: #check if the dict contains the word
            self.wordIDs[stemWord] = self.currWordId #if the word is not present we add the word to the dict along with the id
            self.currWordId += 1 #increment the id for the next word

    def getWordId(self, word):
        stemWord = self.stemmer.stem(word)#getting the stemmed form of the given word
        return self.wordIDs.get(stemWord, None)#returning the ID of the stemmef word
    
    def fetch_d(self):#this method will be used in main.py to fetch all ids that will be written to the output file
        words = self.wordIDs
        sorted_wordIDs = dict(sorted(words.items(), key=lambda item: item[1]))
        return sorted_wordIDs