import os
import xml.dom.minidom as xdm

date = 'DATE'
pro = 'PROFILE'
DOC = 'DOCNO'
path = './ft911/'

class DocParser(object):
    def convert(val):
        doc = xdm.parseString(val)
        root = doc.documentElement
        docs = {}

        for doc in root.childNodes:
            for ele in doc.childNodes:
                if(ele.nodeType == ele.ELEMENT_NODE):
                    if ele.tagName == date or ele.tagName == pro:
                        continue
                    elif ele.tagName == DOC:
                        DOCNO = ele.firstChild.data.strip()
                        docs[DOCNO] = []
                    else:
                        docs[DOCNO].append(ele.firstChild.data.strip())
        return docs
    
    
    def fetchDocs(file):
        with open(os.path.join(path, file), 'r') as File:
            data = File.read()
        full_data = '<DOC>' + data + '</DOC>'
        docs = DocParser.convert(full_data)
        return docs

