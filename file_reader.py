"""
TALK ABOUT STUFF
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
from n_gram import n_gram


def read_file():
    """Reads Bob Ross scripts and makes a list of all the words in the text in order."""
    i = 1
    total_texts = []
    while(i <= 13):
        file_name = "./bob_ross_season_scripts/s28/s28ep" + str(i) + ".txt"
        file = open(file_name)
        text = file.read()
        text = text.replace('.', '')
        text = text.replace(',', '')
        text = text.replace('-', '')
        text = text.replace('(', '')
        text = text.replace(')', '')
        text = text.replace('?', '')
        text = text.replace('\"', '')
        text = text.replace('\'', '')
        text = text.split()
        total_texts.extend(text)
        i += 1 
    return total_texts


def make_n_gram(words_from_text):
    """Using the list of words from the Bob Ross Scripts, create the n-gram for the text"""
    ngram = n_gram(gram={}, words=words_from_text)
    num = len(words_from_text)
    i = 0
    while(i < num-3):
        word_tuple = (words_from_text[i], words_from_text[i+1])
        following_word = (words_from_text[i+2])
        ngram.add_to_ngram(word_tuple, following_word)
        i += 1
    return ngram
