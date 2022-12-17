import os

bookPath = "./books"
encodCp = "utf8"

def __readTextFile(filePath: str):
    with open(filePath, 'r', encoding = encodCp) as file:
        contents = file.read()   
        sentences = contents.split('.') 
    return sentences    

def readTextFiles():
    dir_list = os.listdir(bookPath)
    texts = [[]]

    for dir in dir_list:
        texts.append(__readTextFile(bookPath + '/' + dir))
    
    return texts
