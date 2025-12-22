
def decode1(word):  # replace every "A" with "o"
    return (word.replace("A", "o"))

def decode2(word):  # return every second letter starting from index 0
    return(word[0::2])

def decode3(sentence):  # find the first space and return the reversed first word + rest of the sentence, last if makes it that if there is no space, everything is reversed
    x = sentence.find(" ")
    return((sentence[:x][::-1] + sentence[x:]) if x != -1 else sentence[::-1])

def decode4(word):
    half = (len(word)) // 2  # Calculate half of the length

    return(word[2:2+half]) # return from index 2 to index 2 + half length


decode1("SchAAl")
decode2("hqovtzdpozgm")
decode3("sepocseleT are too expensive")
decode4("ppdolfijnnjifl")