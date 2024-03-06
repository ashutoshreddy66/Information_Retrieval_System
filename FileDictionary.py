folder = './ft911/'
all_file_names = []

class FileDictionary:
    #similar to WordDictionary we do the initialize step
    def __init__(self, path):
        self.fileIDs = {} #dict for all file ids
        self.currFileId = 1#start with id 1 for files
        self.folder = path#set a foldder ref with the given path

    def getFileId(self, file):
        return self.fileIDs.get(file, None)#return the ID of the file(DOCNO) for a given file
    
    def getAllFiles(self):
        return self.fileIDs#returns all the files(DOCNOS)
    
    
    def appendFiles(self, file):
         self.fileIDs[file] = self.currFileId#appending the file(docno) along with a new id
         self.currFileId += 1#incrementing the id

