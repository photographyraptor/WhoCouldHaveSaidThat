from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer

def countVectorizer(text: list):
    vectorizer = CountVectorizer()
    vectorizer.fit(text)
    # print(vectorizer.vocabulary_)
    vector = vectorizer.transform(text)
    # print(vector.shape)
    # print(vector.toarray())

def tfidVectorizer(text: list):    
    vectorizer = TfidfVectorizer()
    vectorizer.fit(text)
    # print(vectorizer.vocabulary_)
    # print(vectorizer.idf_)
    vector = vectorizer.transform(text)  
    # print(vector.shape)
    # print(vector.toarray())

def hashingVectorizer(text: list):
    vectorizer = HashingVectorizer(n_features=20)
    vector = vectorizer.transform(text)
    # print(vector.shape)
    # print(vector.toarray())