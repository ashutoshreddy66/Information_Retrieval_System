import nltk
from nltk.stem import PorterStemmer

# Download the Porter Stemmer data (you only need to do this once)
nltk.download('punkt')

# Create a Porter Stemmer object
porter_stemmer = PorterStemmer()

# Example: Stemming a list of words
word_list = ["wonder", "wondered", "wondering", "wonderfully"]

# Stem each word in the list
stemmed_list = [porter_stemmer.stem(word) for word in word_list]

# Print the original and stemmed words
for original, stemmed in zip(word_list, stemmed_list):
    print(f"Original word: {original}, Stemmed word: {stemmed}")
