def spellcheck(document, valid_words):

    valid_words_set=set(valid_words)
    new_set=set()

    words=document.split()
    
    for word in words:
        word=word.lower()
        if word not in valid_words_set:
            new_set.add(word)
    return new_set




