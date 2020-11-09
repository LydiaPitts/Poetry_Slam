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

This file reads in the Bob Ross script files and creates the ngram object.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
from n_gram import n_gram
import re

def read_file():
    """Reads Bob Ross scripts and makes a list of all the words in the text in order
    excluding punctuation and special characters."""
    i = 1
    total_texts = []
    while i <= 13:
        file_name = "./bob_ross_season_scripts/s28/s28ep" + str(i) + ".txt"
        with open(file_name) as bob_ross_file:
            text = bob_ross_file.read()
            text = re.sub('[\.\?(),"!_\']', "", text)
            text = text.split()
            total_texts.extend(text)
            i += 1 
    return total_texts


def make_n_gram(words_from_text):
    """Using the list of words from the Bob Ross Scripts, create the bigram for the text"""
    ngram = n_gram(gram={}, words=words_from_text)
    num = len(words_from_text)
    i = 0
    while i < num-3:
        word_tuple = (words_from_text[i], words_from_text[i+1])
        following_word = (words_from_text[i+2])
        ngram.add_to_ngram(word_tuple, following_word)
        i += 1
    return ngram
