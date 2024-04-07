import os
import xml.dom.minidom as xdm

date = 'DATE'
pro = 'PROFILE'
DOC = 'DOCNO'
TEXT = 'TEXT'
doc_tag = ['<DOC>', '</DOC>']
read_mode = 'r'

class TextParser(object):
    def convert(val):#method will be used by the fetchdocs() method below to fetch all docnos and complete data
        doc = xdm.parseString(val)#using xdm library to manipulate/parse the input files
        root = doc.documentElement#gets the root element
        docs = {}#declaring a dict to store all data

        for doc in root.childNodes:#iterating through all docs
            for ele in doc.childNodes:#iiterating through all elements in docs
                if(ele.nodeType == ele.ELEMENT_NODE):#check if the nodetype of the element is node element itself
                    if ele.tagName == date or ele.tagName == pro:#ignoring all elements that are not docno
                        continue
                    elif ele.tagName == DOC:#if the element is docno then we add it to out dict
                        DOCNO = ele.firstChild.data.strip()
                        docs[DOCNO] = []
                    elif ele.tagName == TEXT:#else we append all the data to that specific docno
                        docs[DOCNO].append(ele.firstChild.data.strip())
        return docs
    
    
    def fetchDocs(path, file):#this method will be used in main.py to get the parsed docnos and doc content
        with open(os.path.join(path, file), read_mode) as File:
            doc_data = File.read()
        full_doc_data = doc_tag[0] + doc_data + doc_tag[1]
        docs = TextParser.convert(full_doc_data)
        return docs

