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
    print(starting_words)
    words = limerick.build_first_line(starting_words)
    words2 = limerick.build_other_lines(words, 2)
    words3 = limerick.build_third_line(words2)
    words4 = limerick.build_other_lines(words3, 4)
    words5 = limerick.build_other_lines(words4, 5)
    print("------", limerick.first_line)
    print("------", limerick.second_line)
    print("------", limerick.third_line)
    print("------", limerick.fourth_line)
    print("------", limerick.fifth_line)

    




if __name__ == "__main__":
    main()
