"""
TALK ABOUT STUFF
"""
import pronouncing
from collections import Counter
import nltk
from n_gram import n_gram
import file_reader as fr




def main():
    text = fr.read_file()
    fr.make_n_gram(text)




if __name__ == "__main__":
    main()
