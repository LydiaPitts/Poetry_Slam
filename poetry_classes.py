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
        self.words_in_structure = 1


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


    def compare_tag(self, curr_tag, tag):
        if(curr_tag == "NOUN"):
                if(tag == "ADJ"):
                    self.words_in_structure += 1
                    return "NOM"
                if(tag == "DET"):
                    self.words_in_structure += 1
                    return "NP"
                if(tag == "NUM" or "ADP"):
                    self.words_in_structure += 1
                    return curr_tag
        if(curr_tag == "NOM"):
            if(tag == "DET"):
                self.words_in_structure += 1
                return "NP"
            if(tag == "NUM" or "ADV"):
                self.words_in_structure += 1
                return curr_tag
        if(curr_tag == "NP"):
            if(tag == "VERB"):
                self.words_in_structure += 1
                return "VP"
            if(tag == "PART"):
                self.words_in_structure += 1
                return "PP"
            if(tag == "ADP"):
                self.words_in_structure += 1
                return curr_tag
        if (curr_tag == "VP"):
            if(tag == "PRON" or "ADV"):
                self.words_in_structure += 1
                return curr_tag
        return tag

    def examine_line(self, tags):
        curr_tag = tags[-1]
        sentence_stack = []
        i = 2
        #print(curr_tag)
        while(i < len(tags) + 1):
            tag = tags[-i]
            curr_tag = self.compare_tag(curr_tag, tag)
            if curr_tag == "VP":
                sentence_stack.append(curr_tag)
            if curr_tag == "NP":
                sentence_stack.append(curr_tag)
            if curr_tag == "PP":
                sentence_stack.append(curr_tag)
            #print(curr_tag)
            i += 1
        total_sentance_structures = len(sentence_stack)
        #print(self.words_in_structure)
        #print(sentence_stack)
        return total_sentance_structures * self.words_in_structure

    def evaluate_rhyme(self):
        if(self.rhyme_a == "the"):
            return False
        if(self.rhyme_b == "the"):
            return False
        if self.rhyme_a in pronouncing.rhymes(self.rhyme_b):
            return False
        first_line = self.first_line.split()
        second_line = self.second_line.split()
        if(first_line[-1] == second_line[-1]):
            return False
        third_line = self.third_line.split()
        fourth_line = self.fourth_line.split()
        if(third_line[-1] == fourth_line[-1]):
            return False
        return True


    def evaluate_lines(self):
        nlp = spacy.load("en_core_web_sm")
        line_1_tags = self.get_tags(nlp(self.first_line))
        line_2_tags = self.get_tags(nlp(self.second_line))
        line_3_tags = self.get_tags(nlp(self.third_line))
        line_4_tags = self.get_tags(nlp(self.fourth_line))
        line_5_tags = self.get_tags(nlp(self.fifth_line))
        self.fitness += self.examine_line(line_1_tags)
        self.fitness += self.examine_line(line_2_tags)
        self.fitness += self.examine_line(line_3_tags)
        self.fitness += self.examine_line(line_4_tags)
        self.fitness += self.examine_line(line_5_tags)


    def evalutate(self):
        if self.evaluate_rhyme():
            self.evaluate_lines()
        #print(self.fitness)
        return self.fitness


    def get_noun(self, line):
        nlp = spacy.load("en_core_web_sm")
        for token in nlp(line):
            if token.pos_ == "NOUN":
                return token.text

    def get_adj(self, line):
        nlp = spacy.load("en_core_web_sm")
        for token in nlp(line):
            if token.pos_ == "ADJ":
                return token.text


    def get_noun_list(self):
        nouns = []
        nouns.append(self.get_noun(self.first_line))
        nouns.append(self.get_noun(self.second_line))
        nouns.append(self.get_noun(self.third_line))
        nouns.append(self.get_noun(self.fourth_line))
        nouns.append(self.get_noun(self.fifth_line))
        to_return = []
        for noun in nouns:
            if noun != None:
                to_return.append(noun)
        if(len(to_return) < 1):
            to_return.append("rock")
        return to_return


    def get_adj_list(self):
        adjectives = []
        adjectives.append(self.get_adj(self.first_line))
        adjectives.append(self.get_adj(self.second_line))
        adjectives.append(self.get_adj(self.third_line))
        adjectives.append(self.get_adj(self.fourth_line))
        adjectives.append(self.get_adj(self.fifth_line))
        to_return = []
        for adj in adjectives:
            if adj != None:
                to_return.append(adj)
        if(len(to_return) < 1):
            to_return.append("litte")
        return to_return


    def get_poem_name(self):
        nouns = self.get_noun_list()
        adjectives = self.get_adj_list()
        #print("nouns: ", nouns)
        #print("adjs: ", adjectives)
        num_nouns = len(nouns)
        num = random.randint(0, num_nouns-1)
        noun = nouns[num]
        num_adj = len(adjectives)
        num = random.randint(0, num_adj-1)
        adj = adjectives[num]
        name = adj + " " + noun
        return "Poem Name: " + name


"""         

def get_tags(self, doc):
        tags = []
        for token in doc:
            tags.append(token.pos_)
        return tags
"""
