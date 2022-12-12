# imports
import os

# const
bookPath = "./books"
encodCp = "utf8"

# defs
def readTextFile(filePath):
    with open(filePath, 'r', encoding = encodCp) as file:
        lines = file.readlines()    
    return lines

def readTextFiles():
    dir_list = os.listdir(bookPath)
    texts = [[]]

    for dir in dir_list:
        texts.append(readTextFile(bookPath + '/' + dir))
    
    return texts