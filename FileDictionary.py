import os
import re

from docnos import extract_docno

folder = './ft911/'
all_file_names = []

class FileDictionary:
    #similar to WordDictionary we do the initialize step
    def __init__(self, path):
        self.fileIDs = {} #dict for all file ids
        self.currFileId = 1#start with id 1 for files
        self.folder = path#set a foldder ref with the given path

    # def getFileId(self, file):
    #     return self.fileIDs.get(file, None)
    
    def getAllFiles(self):
        return self.fileIDs
    
    
    def appendFiles(self):
        Files = os.listdir(self.folder) #setup all the files from the folder 
        for File in Files:
            if(File.startswith("ft911_")): #looping over all files to see if it starts with ft911
                file_path = os.path.join(folder, File)
                docnos = extract_docno(file_path)
                all_file_names.extend(docnos)
                for fileName in all_file_names:
                    # print(fileName, self.currFileId)
                    self.fileIDs[fileName] = self.currFileId
                    self.currFileId += 1 #increment the id for the next word

                # self.fileIDs[File] = self.currFileId #if condiction is satisified we add it to our dict along with an ID
                
# obj = FileDictionary(folder)
# obj.appendFiles()
# var = obj.getAllFiles()
# print(var)

