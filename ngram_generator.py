"""
Author: Lydia Pitts
CSCI 3725: Computational Creativity
Mission 6: Poetry Slam

_____
"""

class Ngram(object):
    """
    Attributes:
        ngram --> nested dictionary where keys are a tuple of two words and the value is 
        a dictionary that contains the word following the two words and the number of times 
        that word appears.
    """
    def __init__(self, gram):
        self.gram = gram


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
        """Adds a tuple of two words as they key to the Ngram, and the word that follows 
        those two words (and the # of times it follows those words) as the value"""



def main():
    Firstgram = Ngram(gram={})
    Firstgram.addToNgram(("hello", "world"), "thanks")
    Firstgram.addToNgram(("hello", "world"), "thanks")
    Firstgram.addToNgram(("hello", "world"), "sure")
    Firstgram.addToNgram(("hello", "there"), "hi")
    


"""
Driver for the entire program
"""
if __name__ == "__main__":
    main()
    
    
    
