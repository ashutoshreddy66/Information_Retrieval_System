import re
import os

all_file_names = []

def extract_docno(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        docno_matches = re.findall(r'<DOCNO>(.*?)<\/DOCNO>', content)
        return docno_matches

folder = './ft911/'

for File in os.listdir(folder):
    if(File.startswith("ft911_")):
        file_path = os.path.join(folder, File)
        docnos = extract_docno(file_path=file_path)
        all_file_names.extend(docnos)


