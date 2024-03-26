import os
from pathlib import Path
from collections import Counter

class Indexer:


    def create_forward_index(index):
        new_forwardIndex = {}
        for docno, text in index.items():
            word_counts = Counter(text)
            new_forwardIndex[docno] = word_counts
        return new_forwardIndex
        

    def write_forward_index(new_forwardIndex, fileName):    
        try:
            filepath = os.path.join(Path(__file__).parent.resolve(), fileName)
            with open(filepath, "w") as fIndex:
                for docno, counts in new_forwardIndex.items():
                    fIndex.write(f"{docno}:\t" +"; ".join([f"{word} {count}" for word, count in counts.items()]))
                    fIndex.write("\n\n")
            print("index success in "+fileName)
        except:
            print(f"index {fileName} failure ")


        
    def create_inverted_index(docs):
        inverted_index = {}
        for docno, wordCounts in docs.items():
            for word, count in wordCounts.items():
                if word not in inverted_index:
                    inverted_index[word] = []
                inverted_index[word].append((docno,count))
        # print(inverted_index)
        return inverted_index
    
    def write_inverted_index(inverted_index, filename):
        try:
            filepath = os.path.join(Path(__file__).parent.resolve(), filename)
            with open(filepath, "w") as iIndex:
                for word, postings in inverted_index.items():
                    iIndex.write(f"{word}:\t"+"; ".join(f"{docno} {count}" for docno, count in postings))
                    iIndex.write("\n\n")
            print("index success in "+filename)
        except:
            print(f"index {filename} failure ")
            