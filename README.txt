#Project Phase 2 README.

##Requirements
- Python 3.0 or later

##Installation
1. To install python, you can go to this website (https://www.python.org/downloads/) and click on the Download button.
2. Unzip the entire folder
3. Open the unzipped folder in an IDE of your choice. 

##Running the code
1. Open 'main.py'
2. Before running the python file to check the output, you must make sure you have the "nltk" library installed. If not, run the command "pip install -U nltk"
3. Once all the dependencies are installed, you can run the file by either clicking on the run button or running 
the command "python main.py" from where the main.py file is located.

##Jupyter notebook(alternative execution)
1. Open 'main.ipynb' in jupyter/colab/vscode
2. Run all cells at once to see the output in the `parser_output.txt`,`forward_index.txt` and 'inverted_index.txt` files.

##Output
- Upon compiling either the python project from main.py or running all the cells using the main.ipynb file you will be able to find the outputs in forward_index.txt that stores all forward indices and inverted_index.txt that stores all inverted indices. 
- The output for forward_index will be in the following format : 
    Document1 : Word1 Count1; Word2 Count2; Word3 Count3;.....
    Document2 : Word1 Count1; Word2 Count2; Word3 Count3;.....
    Document3 : Word1 Count1; Word2 Count2; Word3 Count3;.....
    
-The output for inverted_index will be in the following format :
    Word1 : Document1 Count1; Document2 Count2; Document3 Count3;......
    Word2 : Document1 Count1; Document2 Count2; Document3 Count3;......
    Word3 : Document1 Count1; Document2 Count2; Document3 Count3;......

##Testing
- For testing the code with a different dataset, please replace the 'path' variable on line 18 in main.py file with the absolute path of the test folder.