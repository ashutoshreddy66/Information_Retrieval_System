import math
import os
import re
import time
from pathlib import Path
from WordDictionary import WordDictionary
from FileDictionary import FileDictionary
from tokenizer import tokenizer
from DocParser import TextParser
from datetime import datetime
from indexer import Indexer
import nltk
from nltk.stem import PorterStemmer

# nltk.download('punkt')


print("Running code at:", datetime.now())

path = "./ft911/"
folder = os.listdir(path=path)

parser_file = "parser_output.txt"
forward_index_file = "forward_index.txt"
inverted_index_file = "inverted_index.txt"
vsm_title_file = "vsm_title.txt"
vsm_desc_file = "vsm_description.txt"
vsm_narr_file = "vsm_narrative.txt"

w = 'w'
a = 'a'

def parser_output(fileName, data, mode):    
    try:#exception handling
        filePath = os.path.join(Path(__file__).parent.resolve(), fileName)#created a file if it doesn't already exist to write output
        with open(filePath, mode) as parser_output:
            for key in data.keys():#iterates through all docnos and stemmed words
                parser_output.write(f"{key}\t{data[key]}\n")#appeninf the DOCNO: DOCID and Word : WOrdID to the parser_output file
        print("Parser output- Success: Writing data COmpleted!: ",fileName)
    except:#shows error message in case of failure
        print("Parser output- Failure: error while uploading data: ", fileName)


#then we initialize our custom dictionaries
WordDict = WordDictionary()
FileDict = FileDictionary(path)


def get_stem_words(forward_words):
    stemmer = PorterStemmer() 
    stemmed_words = []
    for word in forward_words:
        stemword = stemmer.stem(word)
        if stemword == "":
            pass
        else:
            stemmed_words.append(stemword)
    return stemmed_words

forwardIndex = {}
forward_tokens = []
#looping over all the files in the folder mentioned above and and adding them to complete data
for file in folder:
    docs = TextParser.fetchDocs(path, file)
    for docno, data in docs.items():
        FileDict.appendFiles(docno)
        tokens = tokenizer(data)
        for token in tokens:
            WordDict.appendWord(token)
        stemmed_words = get_stem_words(tokens)
        forwardIndex[docno] = stemmed_words

start_parser = time.time()
wordData = WordDict.fetch_d()
fileData = FileDict.getAllFiles()
parser_output(parser_file, wordData, w)#once all the word data is feteched, we write the data to the output file using the 'w' mode
parser_output(parser_file, fileData, a)#once all the filenames are feteched, we append the data to the output file using the 'a' mode
end_parser = time.time()

total_parser_time = end_parser - start_parser
print(f"Time taken for Parsing the documents = {total_parser_time} seconds")

start_time = time.time()
new_forwardIndex = Indexer.create_forward_index(forwardIndex)
Indexer.write_forward_index(new_forwardIndex, forward_index_file)

inverted_index = Indexer.create_inverted_index(new_forwardIndex)
Indexer.write_inverted_index(inverted_index, inverted_index_file)
end_time = time.time()

execution_time = end_time - start_time
print(f"Time taken to generate the indexes is {execution_time} seconds.")
print(f"Total number of words = {len(inverted_index)}")
print(f"Total number of documents = {len(new_forwardIndex)}")

def test_function():
    text = input("Enter a word you want to search: ")

    if text not in inverted_index:
        print("The word you are searching for is not present in the index!")
    else:
       info = inverted_index.get(text)
       completeInfo = ""
       for docno, count in info:
           completeInfo += docno+ " "+str(count)+"; "
       print(f"{text}:\t{completeInfo}")
           

def query_parser():#method used for parsing the content of topics.txt
    topic_path = Path(__file__).parent.resolve() / "topics.txt"
    input = topic_path.read_text()#gets all content

    quries = re.split(r'</top>', input)
    quries = [q.strip() for q in quries if q.strip()]

    result = {}
    for i,q_text in enumerate(quries):
        Match = re.search(r'<num> Number: (\d+).*?<title> (.+?)<desc> Description:(.*?)<narr> Narrative:(.*?)$', q_text, flags=re.DOTALL)
        if Match:
            dictionary = {'title':Match.group(2).strip(), 'description':Match.group(3).strip(), 'narrative': Match.group(4).strip()}
            result[int(Match.group(1))] = dictionary
    return result

def getCosineScore(query):#calculates the cosine score for a given query
    scores = {}
    document_len = {}
    query_len = 0
    for query_term in query:
        stemmed_query_term = inverted_index.get(PorterStemmer().stem(query_term))
        if stemmed_query_term is not None:
            documents = dict(stemmed_query_term)
        if documents is not None:
            idf = math.log(len(new_forwardIndex))/len(documents)
            query_len += idf**2
            for document in documents.keys():
                if document_len.get(document) is None:
                    document_len[document] = math.sqrt(sum(((tf * math.log(len(new_forwardIndex)/len(inverted_index[term_id])))**2)for
                                                term_id, tf in new_forwardIndex[document].items()))
                if fileData[document] not in scores:
                    scores[fileData[document]] = 0
                scores[fileData[document]] += documents[document]/document_len[document] * idf

    for document in scores.keys():
        scores[document] /= math.sqrt(query_len)

    return scores                    

queryList = query_parser()
# print(queryList)

print(f"Calculating cosine score for queryList")
vsm_title = open(os.path.join(Path(__file__).parent.resolve(), vsm_title_file), w)
vsm_desc = open(os.path.join(Path(__file__).parent.resolve(), vsm_desc_file), w)
vsm_narr = open(os.path.join(Path(__file__).parent.resolve(), vsm_narr_file), w)
for topicNumber, query in queryList.items():
    i = 0
    j = 0
    k = 0 
    wordsList = [tokenizer([query['title']]), tokenizer([query['description']]), tokenizer([query['narrative']])]
    stemmer = PorterStemmer()
    for words in wordsList:
        [stemmer.stem(word) for word in words]
    titles = getCosineScore(wordsList[0])
    descriptions = getCosineScore(wordsList[0]+wordsList[1])
    narratives = getCosineScore(wordsList[0]+wordsList[2])

    # print(titles)
    # print(descriptions)
    # print(narratives)

    for docNo, value in titles.items():
        vsm_title.write(f"{topicNumber}\t{FileDict.getFileName(docNo)}\t{i+1}\t{value}\n")
        i += 1
    
    for docNo, value in descriptions.items():
        vsm_desc.write(f"{topicNumber}\t{FileDict.getFileName(docNo)}\t{j+1}\t{value}\n")
        j += 1
    
    for docNo, value in narratives.items():
        vsm_narr.write(f"{topicNumber}\t{FileDict.getFileName(docNo)}\t{k+1}\t{value}\n")
        k += 1

vsm_title.close()
vsm_desc.close()
vsm_narr.close()
# test_function()

print("Finished writing cosine scores")