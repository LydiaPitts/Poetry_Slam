"""
TALK ABOUT STUFF
"""
import pronouncing
from collections import Counter
import nltk
from n_gram import n_gram
import file_reader as fr
from poetry_classes import Limerick



def main():
    text = fr.read_file()
    ngram = fr.make_n_gram(text)

    limerick = Limerick(ngram)
    starting_words = ngram.get_starting_words()
    limerick.build_full_limerick(starting_words)
    limerick.print_limerick()
    limerick.evalutate() 

if __name__ == "__main__":
    main()
