"""
TALK ABOUT STUFF
"""
import pronouncing
from collections import Counter
import nltk
from n_gram import n_gram
import file_reader as fr
from poetry_classes import Limerick
import make_html as html


def make_limerick(ngram):
    limerick = Limerick(ngram)
    starting_words = ngram.get_starting_words()
    limerick.build_full_limerick(starting_words)
    #limerick.print_limerick()
    limerick.evalutate()
    return limerick


def get_limericks_above_100(ngram):
    top_limericks = []
    while len(top_limericks) < 2:
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
    poem_name = limerick.get_poem_name()
    separate_name = poem_name.split()
    poem_name = separate_name[0] + "_" + separate_name[1]
    line1 = limerick.first_line
    line2 = limerick.second_line
    line3 = limerick.third_line
    line4 = limerick.fourth_line
    line5 = limerick.fifth_line
    html.make_html_doc(poem_name, line1, line2, line3, line4, line5)


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

