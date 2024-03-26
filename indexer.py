import os
from pathlib import Path
from collections import Counter

class Indexer:


    def create_forward_index(index):
        new_forwardIndex = []
        for docno, text in index.items():
            word_counts = Counter(text)
            new_forwardIndex.append((docno, word_counts))
        return new_forwardIndex
        

    def write_forward_index(new_forwardIndex):
        forward_index = "forward_index.txt"
        try:
            filepath = os.path.join(Path(__file__).parent.resolve(), forward_index)
            with open(filepath, "w") as fIndex:
                for docno, counts in new_forwardIndex:
                    fIndex.write(f"{docno}:\t" +"; ".join([f"{word} {count}" for word, count in counts.items()]))
                    fIndex.write("\n\n")
            print("forward_index success")
        except Exception as e:
            print("forward_index failure : "+e)


        
    def create_inverted_index(docs):
        inverted_index = {}
        for docno, wordCounts in docs:
            for word, count in wordCounts.items():
                if word not in inverted_index:
                    inverted_index[word] = []
                inverted_index[word].append((docno,count))
        return inverted_index