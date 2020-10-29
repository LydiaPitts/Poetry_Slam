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
        return pronouncing.syllable_count(pronunciation_list[0])


    def build_first_or_third(self, starting_words, line_number):
        syllables = 0
        line = ""
        syllable_num = 6
        if(line_number == 3):
            syllable_num = 4
        while syllables < syllable_num:
            next_word = self.n_gram.retreive_next_word(starting_words)
            syllables += self.get_syllables(next_word)
            line += next_word  + " "
            starting_words = (starting_words[1], next_word)
        next_word = self.n_gram.retreive_next_word(starting_words)
        line += next_word
        if line_number == 1:
            self.first_line = line
            self.rhyme_a = next_word
            #print(line, " = " + self.rhyme_a)
        else:
            self.third_line = line
            self.rhyme_b = next_word
            #print(line, " = " + self.rhyme_b)
        starting_words = (starting_words[1], next_word)
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
        #print(line, " = " + rhyme)
        starting_words = (starting_words[1], next_word)

        if line_number == 2:
            self.second_line = line
        elif line_number == 4:
            self.fourth_line = line
        else:
            self.fifth_line = line
        return starting_words

    
    def evalutation(self):
        # Parse Tree?
        #    ^ evaluate the gramatical structure??
        # Alliteration, assonance 
        #    ^ for style purposes?
        # Meeter?
        #    ^ evaluate the "flow" of the poem?
        return 0