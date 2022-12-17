# imports
import os
from sklearn.feature_extraction.text import CountVectorizer

# const
bookPath = "./books"
encodCp = "utf8"

# defs priv
def __readTextFile(filePath: str):
    with open(filePath, 'r', encoding = encodCp) as file:
        contents = file.read()   
        sentences = contents.split('.') 
    return sentences
    
def __wordCountLine(line: str, vectorizer):
    vectorizer.fit(line)
    vector = vectorizer.transform(line)
    return vector

# defs
def readTextFiles():
    dir_list = os.listdir(bookPath)
    texts = [[]]

    for dir in dir_list:
        texts.append(__readTextFile(bookPath + '/' + dir))
    
    return texts

def wordCountLines(lines):
    vectors = [[]]
    vectorizer = CountVectorizer()    

    
    vectors.append(__wordCountLine(lines[1], vectorizer))

    #for line in lines:
     #   vectors.append(__wordCountLine(line, vectorizer))

    print(vectorizer.vocabulary_)
