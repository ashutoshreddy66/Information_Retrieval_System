import re
import os

all_file_names = []

def extract_docno(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        # Use regular expression to find content between <DOCNO> tags
        docno_matches = re.findall(r'<DOCNO>(.*?)<\/DOCNO>', content)
        # print("type of :", type(docno_matches))
        return docno_matches

# Example usage:
folder = './ft911/'

for File in os.listdir(folder):
    if(File.startswith("ft911_")):
        file_path = os.path.join(folder, File)
        # print(file_path)
        docnos = extract_docno(file_path=file_path)
        all_file_names.extend(docnos)

# print(all_file_names)

