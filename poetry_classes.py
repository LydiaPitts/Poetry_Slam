"""
WRITE THINGS
"""

import random
import pronouncing
from n_gram import n_gram

class Limerick(object):
    """
    Attributes:
        
    """

    def __init__(self, n_gram):
        self.first_line = ""
        self.second_line = ""
        self.third_line = ""
        self.fourth_line = ""
        self.fifth_line = ""
        self.rhyme_a = ""
        self.rhyme_b = ""
        self.n_gram = n_gram

    def get_syllables(self, word):
        word = str(word)
        pronunciation_list = pronouncing.phones_for_word(word)
        if(len(pronunciation_list) < 1):
            return 1
        #print(word)
        #print(pronunciation_list)
        return pronouncing.syllable_count(pronunciation_list[0])


    def build_first_line(self, starting_words):
        #print("Start Line 1: ")
       # print(starting_words)
        syllables = self.get_syllables(starting_words[0]) + self.get_syllables(starting_words[1])
        self.first_line = str(starting_words[0]) + " " + str(starting_words[1])
        while syllables < 6:
            next_word = self.n_gram.retreive_next_word(starting_words)
            syllables += self.get_syllables(next_word)
            self.first_line += " " + next_word
            starting_words = (starting_words[1], next_word)
        next_word = self.n_gram.retreive_next_word(starting_words)
        self.first_line += " " + next_word
        self.rhyme_a = next_word
        print(self.first_line, " = " + self.rhyme_a)
        starting_words = (starting_words[1], next_word)
        #print(starting_words)
        #print("^^^^^^")
        return starting_words
    
    def build_third_line(self, starting_words):
        #print("Start line 3: ")
       # print(starting_words)
        syllables = 0
        while syllables < 4:
            next_word = self.n_gram.retreive_next_word(starting_words)
            syllables += self.get_syllables(next_word)
            self.third_line += next_word + " "
            starting_words = (starting_words[1], next_word)
        next_word = self.n_gram.retreive_next_word(starting_words)
        self.third_line += next_word
        self.rhyme_b = next_word
        print(self.third_line, " = " + self.rhyme_b)
        starting_words = (starting_words[1], next_word)
        #print(starting_words)
        #print("^^^^^^")
        return starting_words



    def build_other_lines(self, starting_words, line_number):
        syllables = 0
        line = ""
        syllable_num = 6
        rhyme = self.rhyme_a

        if(line_number == 4):
            syllable_num = 4
            rhyme = self.rhyme_b

        while syllables < syllable_num:
            next_word = self.n_gram.retreive_next_word(starting_words)
            syllables += self.get_syllables(next_word)
            line += next_word + " "
            starting_words = (starting_words[1], next_word)
        
        next_word = self.n_gram.retreive_ryming_word(starting_words, rhyme)
        line += next_word
        print(line, " = " + rhyme)
        starting_words = (starting_words[1], next_word)
        #print(starting_words)
        #print("^^^^^^")
        if line_number == 2:
            self.second_line = line
        elif line_number == 4:
            self.fourth_line = line
        else:
            self.fifth_line = line
        return starting_words, line



    


def main():
    Firstgram = n_gram(gram={}, words=["hello", "world", "there", "thank", "hi"])
    Firstgram.add_to_ngram(("hello", "world"), "thank")
    Firstgram.add_to_ngram(("world", "sure"), "thank")
    Firstgram.add_to_ngram(("world", "thank"), "sure")
    Firstgram.add_to_ngram(("thank", "sure"), "hi")
    limerick = Limerick(n_gram=Firstgram)
    next_words = limerick.build_first_line(("hello", "world"))
    limerick.build_third_line(("hello", "world"))


"""
Driver for the entire program
"""
if __name__ == "__main__":
    main()