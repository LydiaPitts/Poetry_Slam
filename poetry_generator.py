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

This file drives the poetry generation process, and includes our main function. This is 
where limericks and their files are actually made.
"""

import pronouncing
from collections import Counter
import nltk
from n_gram import n_gram
import file_reader as fr
from poetry_classes import Limerick
import make_html as html

def make_limerick(ngram):
    """Carries out all the functions to make a limerick object useful, and then returns the poem object"""
    limerick = Limerick(ngram)
    starting_words = ngram.get_starting_words()
    limerick.build_full_limerick(starting_words)
    limerick.evalutate()
    return limerick


def get_limericks_above_100(ngram):
    """Continuously loops until it creates a list of 5 poem with a fitness scoring above 100"""
    top_limericks = []
    while len(top_limericks) < 5:
        limerick = make_limerick(ngram)
        add_limerick = False
        if limerick.fitness > 100:
            add_limerick = True
        for poem in top_limericks:
            if poem.first_line == limerick.first_line:
                add_limerick = False
        if add_limerick:
            print("added Limerick")
            top_limericks.append(limerick)
    return top_limericks


def create_files(limerick):
    "Makes an html file with the information from a given limerick"
    poem_name = limerick.get_poem_name()
    separate_name = poem_name.split()
    file_name = separate_name[0] + "_" + separate_name[1]
    line1 = limerick.first_line
    line2 = limerick.second_line
    line3 = limerick.third_line
    line4 = limerick.fourth_line
    line5 = limerick.fifth_line
    html.make_html_doc(poem_name, file_name, line1, line2, line3, line4, line5)


def main():
    text = fr.read_file()
    ngram = fr.make_n_gram(text)
    top_poems = get_limericks_above_100(ngram)
    print("_________________________________________")
    for poem in top_poems:
        print("_________________")
        print(poem.get_poem_name())
        poem.print_limerick()
        print(poem.fitness)
        create_files(poem)
        print("_________________")


if __name__ == "__main__":
    main()

