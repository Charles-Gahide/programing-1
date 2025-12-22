'''
def decode1(word):  # replace every "A" with "o"
    return (word.replace("A", "o"))

def decode2(word):  # return every second letter starting from index 0
    return(word[0::2])

def decode3(sentence):  # find the first space and return the reversed first word + rest of the sentence, last if makes it that if there is no space, everything is reversed
    x = sentence.find(" ")
    return((sentence[:x][::-1] + sentence[x:]) if x != -1 else sentence[::-1])

def decode4(word):
    half = len(word) // 2
    return word[2:2 + half][::2]

def decode5(sentence):
    sentence = decode3(sentence)  # Strategy 3

    words = sentence.split()
    words = [decode4(word) for word in words]  # Strategy 4
    words = [decode2(word) for word in words]  # Strategy 2
    words = [decode1(word) for word in words]  # Strategy 1

    return ' '.join(words)
print(decode5("MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu""MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu"))
'''



def decode1(word):
    return word.replace("A", "o")

def decode2(word):
    return word[::2]

def decode3(word):
    x = word.find(" ")
    return (word[:x][::-1] + word[x:]) if x != -1 else word[::-1]

def decode4(word):
    half = len(word) // 2
    return word[2:2 + half][::2]

def decode5(sentence):
    words = sentence.split()
    decoded_words = []
    for word in words:
        w0 = decode4(word)
        w1 = decode2(w0)
        w2 = decode1(w1)
        w3 = decode3(w2)
        decoded_words.append(w3)
    return ' '.join(decoded_words)

# Test it
print(decode5("MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu"))

    
   
       
   

print(decode5("MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu"))


