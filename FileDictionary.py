import os
import re


folder = './ft911/'
all_file_names = []

class FileDictionary:
    #similar to WordDictionary we do the initialize step
    def __init__(self, path):
        self.fileIDs = {} #dict for all file ids
        self.currFileId = 1#start with id 1 for files
        self.folder = path#set a foldder ref with the given path

    def getFileId(self, file):
        return self.fileIDs.get(file, None)
    
    def getAllFiles(self):
        return self.fileIDs
    
    
    def appendFiles(self, file):
         self.fileIDs[file] = self.currFileId
         self.currFileId += 1

