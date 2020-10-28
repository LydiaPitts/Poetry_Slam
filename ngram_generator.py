"""
Author: Lydia Pitts
CSCI 3725: Computational Creativity
Mission 6: Poetry Slam

_____
"""

import random
import pronouncing
import string

class Ngram(object):
    """
    Attributes:
        ngram --> nested dictionary where keys are a tuple of two words and the value is 
        a dictionary that contains the word following the two words and the number of times 
        that word appears.
    """

    def __init__(self, gram, words):
        self.gram = gram
        self.words = words

    def addToNgram(self, twoWords, followingWord):
        """Adds a tuple of two words as they key to the Ngram, and the word that follows 
        those two words (and the # of times it follows those words) as the value"""
        following = {}
        if(twoWords in self.gram):
            following = self.gram[twoWords]
            if(followingWord in following.keys()):
                following[followingWord] += 1
            else:
                following.setdefault(followingWord, 1)
            self.gram[twoWords] = following
            #print(self.gram[twoWords])
        else:
            following.setdefault(followingWord, 1)
            self.gram.setdefault(twoWords, following)
            #print(self.gram[twoWords])

    def retreiveNextWord(self, twoWords):
        """Based on the two given words (in the form of a tuple) selects the next word 
        probabilistically"""
        if(twoWords in self.gram):
            following = self.gram[twoWords]
            word_probabilities = []
            for key in following.keys():
                j = 0
                while(j < following[key]):
                    word_probabilities.append(key)
                    j += 1
            num = random.randint(0, len(word_probabilities)-1)
            return word_probabilities[num]
        else:
            num = random.randint(0, len(self.words)-1)
            return self.words[num]


    def retreiveRymingWord(self, twoWords, wordToRhymeWith):
        """Based on the two given words (in the form of a tuple) selects the next word 
        that rhymes probabilistically"""
        rhymes = pronouncing.rhymes(wordToRhymeWith.lower())
        print(rhymes)
        if(twoWords in self.gram):
            following = self.gram[twoWords]
            word_probabilities = []
            for key in following.keys():
                if(key in rhymes):
                    j = 0
                    while(j < following[key]):
                        word_probabilities.append(key)
                        j += 1
            if(len(word_probabilities) > 0):
                num = random.randint(0, len(word_probabilities)-1)
                #print(word_probabilities[num], " = next character rhyme")
                return word_probabilities[num]
        num = random.randint(0, len(rhymes))
        #print(rhymes[num] + " = rand rhyme")
        return rhymes[num]





def main():
    Firstgram = Ngram(gram={}, words=["word", "word2", "word3"])
    Firstgram.addToNgram(("hello", "world"), "thank")
    Firstgram.addToNgram(("hello", "world"), "thank")
    Firstgram.addToNgram(("hello", "world"), "sure")
    Firstgram.addToNgram(("hello", "there"), "hi")
    Firstgram.retreiveNextWord(("hello", "world"))
    Firstgram.retreiveRymingWord(("hello", "world"), "SPank")
    

if __name__ == "__main__":
    main()
    
    
    
