"""
Author: Lydia Pitts
CSCI 3725: Computational Creativity
Mission 6: Poetry Slam
Last Edited: Nov 1, 2020

The purpose of this program is to write limericks inspired from Bob Ross's season 28 youtube 
transcripts that are then evaluated and eventually displayed on the brouser. This program
utilizes n-grams, parse trees as well as other characteristics of limericks and topics we 
have discussed in class. I have named my program LACTIC - Limericks Accessed Creatively
Through Intentional Computation

This file contains the n_gram class and all of it's associated functions. In this case it
is a bigram, and this class offers the appropriate access to information. Other classes are
able to retrive words based on probabilities and specifications, as well as add to the bigram.
"""


import random
import pronouncing
import string

class n_gram(object):
    """
    Attributes:
    gram -- nested dictionary where keys are a tuple of two words and the value is a dictionary 
    that contains the word following the two words and the number of times that word appears
    words -- a list of all the words found in the inspiring set (not nessecarily ordered)
    """

    def __init__(self, gram, words):
        self.gram = gram
        self.words = words

    def add_to_ngram(self, two_words, following_word):
        """Adds a tuple of two words as they key to the Ngram, and the word that follows 
        those two words (and the # of times it follows those words) as the value"""
        following = {}
        if(two_words in self.gram):
            following = self.gram[two_words]
            if(following_word in following.keys()):
                following[following_word] += 1
            else:
                following.setdefault(following_word, 1)
            self.gram[two_words] = following
        else:
            following.setdefault(following_word, 1)
            self.gram.setdefault(two_words, following)


    def retreive_next_word(self, two_words):
        """Based on the two given words (in the form of a tuple) selects the next word 
        probabilistically"""
        if(two_words in self.gram):
            following = self.gram[two_words]
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


    def retreive_ryming_word(self, two_words, word_to_rhyme_with):
        """Based on the two given words (in the form of a tuple) selects the next word 
        that rhymes probabilistically"""
        rhymes = pronouncing.rhymes(word_to_rhyme_with.lower())
        if(two_words in self.gram):
            following = self.gram[two_words]
            word_probabilities = []
            for key in following.keys():
                if(key in rhymes):
                    j = 0
                    while(j < following[key]):
                        word_probabilities.append(key)
                        j += 1
            if(len(word_probabilities) > 0):
                num = random.randint(0, len(word_probabilities)-1)
                return word_probabilities[num]
        if len(rhymes) < 1:
            return word_to_rhyme_with
        num = random.randint(0, len(rhymes)-1)
        return rhymes[num]


    def get_starting_words(self):
        """Get two random starting words from within the text"""
        num = random.randint(0, len(self.gram)-1)
        keys = list(self.gram)
        return tuple(keys[num])


