"""
WRITE THINGS
"""

import random
import pronouncing
from n_gram import n_gram
import spacy

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
        self.fitness = 0


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


    def build_full_limerick(self, starting_words):
        words01 = self.build_first_or_third(starting_words, 1)
        words02 = self.build_other_lines(words01, 2)
        words03 = self.build_first_or_third(words02, 3)
        words04 = self.build_other_lines(words03, 4)
        words05 = self.build_other_lines(words04, 5)

    def print_limerick(self):
        print(self.first_line)
        print(self.second_line)
        print(self.third_line)
        print(self.fourth_line)
        print(self.fifth_line)

    
    def get_tags(self, doc):
        tags = []
        for token in doc:
            tags.append(token.pos_)
        return tags


    def compare_tags(self, tags):
        curr_tag = tags[-1]
        sentence_stack = []
        words_in_structures = 1
        i = 2
        print(curr_tag)
        while(i < len(tags) + 1):
            tag = tags[-i]
            if(curr_tag == "NOUN"):
                if(tag == "ADJ"):
                    print("got here 1")
                    curr_tag = "NOM"
                    words_in_structures += 1
                if(tag == "DET"):
                    print("got here 2")
                    curr_tag = "NP"
                    sentence_stack.append("NP")
                    words_in_structures +=1
                if(tag == "NUM"):
                    print("got here 3")
                    words_in_structures += 1
                if(tag == "ADP"):
                    print("got here 4")
                    words_in_structures += 1
                else:
                    curr_tag = tag

            if(curr_tag == "NOM"):
                if(tag == "DET"):
                    curr_tag = "NP"
                    sentence_stack.append("NP")
                    words_in_structures += 1
                if(tag == "NUM"):
                    words_in_structures += 1
                if(tag == "ADV"):
                    words_in_structures += 1
                else:
                    curr_tag = tag

            if(curr_tag == "NP"):
                if(tag == "VERB"):
                    curr_tag = "VP"
                    sentence_stack.append("VP")
                    words_in_structures += 1
                if(tag == "PART"):
                    curr_tag = "PP"
                    words_in_structures += 1
                else:
                    curr_tag = tag

            if (curr_tag == "VP"):
                if(tag == "PRON"):
                    words_in_structures += 1
                if(tag == "ADV"):
                    words_in_structures += 1
                else:
                    curr_tag = tag

            else:
                curr_tag = tag
            print(curr_tag)
            i += 1
        print(words_in_structures)
        print(sentence_stack)
        return 0

    def evalutate(self):
        print("__________________________________")
        print("I'm evalutaing now:")
        nlp = spacy.load("en_core_web_sm")
        line_1_tags = self.get_tags(nlp(self.first_line))
        line_2_tags = self.get_tags(nlp(self.second_line))
        line_3_tags = self.get_tags(nlp(self.third_line))
        line_4_tags = self.get_tags(nlp(self.fourth_line))
        line_5_tags = self.get_tags(nlp(self.fifth_line))
        print(self.first_line)
        print(line_1_tags)
        self.compare_tags(line_1_tags)
        



        # Parse Tree
        #    ^ evaluate the gramatical structure
        
        return 0





# Alliteration, assonance 
        #    ^ for style purposes?
        # Meter?
        #    ^ evaluate the "flow" of the poem?