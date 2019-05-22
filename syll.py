#syllable checker
vowels = ['a','e','i','o','u','y']

'''counter words
ion/scion/etc
peaceful/etc
miscreant, -ea- is kind of random (create, etc)
'''

def charCheck( word, i ): #should return bool
    if i == 0: #first character
        if word[i] == 'y':
            return False
        else:
            return True
    elif i == len(word)-1: #last character
        if word[i] == 'e' and not word[i-1] == 'l' and not word[i-2] == 'b':
            return False
        if word[i] == 'y' and word[i-1] in vowels:
            return False
        if word[i] in vowels[:4] and word[i-1] in vowels[:4]:
            if word[i] == 'o':
                if word[i-1] == 'e' or word[i-1] == 'i':
                    return True
            elif word[i] == 'a' and word[i-1] == 'i':
                return True
            else:
                return False
        else:
            return True
    else: #a middle character
        if word[i-1] == word[i]:
            return False
        if word[i] in vowels[:5] and word[i-1] in vowels[:5]:
            if word[i] == 'o':
                if word[i-1] == 'e' or word[i-1] == 'i':
                    return False if word[i+1] == 'n' else True
            elif word[i] == 'a' and word[i-1] == 'i':
                return True
            else:
                return False
        if i >= 2:
            if word[i-1] == 'u' and word[i-2] == 'q':
                return False
        if i == len(word)-2 and word[i] == 'e' and word[i+1] == 'd':
            return False
        return True


def sylCheck( word ):
    sylls = 0
    for i in range( len(word) ):
        if word[i] in vowels:
            sylls += charCheck( word, i )
    return sylls

def noPossession( word ):
    subtractors = ['\'s', 'cial', 'cius', 'cious', 'uiet', 'gious', 'geous', 'priest', 'giu', 'tia']
    for stri in subtractors:
        if word.endswith(stri):
            return word[:-len(stri)] + 'o'
    return word

def sentenceCheck( sentence ):
    return sum([sylCheck(noPossession(word)) for word in sentence.lower().split(' ')])

if __name__ == "__main__":
    print( "enter a sentence" )
    print( sentenceCheck(input()) )
