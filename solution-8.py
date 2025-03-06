def createDict(shift):
    CodeDict={}
    for letter in range (0,26):
        shifted_letter = (letter+shift)%26
        CodeDict[chr(letter+97)]= chr(shifted_letter+97)
    return CodeDict

def encrypt(input):
    Dict = createDict(10)
    result = []
    for letter in input:
        result.append(Dict[letter])
    return ''.join(result)

def decrypt(input):
    Dict = createDict(26-10)
    result = []
    for letter in input:
        result.append(Dict[letter])
    return ''.join(result)
