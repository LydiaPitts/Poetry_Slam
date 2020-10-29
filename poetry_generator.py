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

    words01 = limerick.build_first_or_third(starting_words, 1)
    words02 = limerick.build_other_lines(words01, 2)
    words03 = limerick.build_first_or_third(words02, 3)
    words04 = limerick.build_other_lines(words03, 4)
    words05 = limerick.build_other_lines(words04, 5)
    print("**********", limerick.first_line)
    print("**********", limerick.second_line)
    print("**********", limerick.third_line)
    print("**********", limerick.fourth_line)
    print("**********", limerick.fifth_line)


if __name__ == "__main__":
    main()
