"""
TALK ABOUT STUFF
"""
import pronouncing
from collections import Counter
import nltk
from n_gram import n_gram
import file_reader as fr
from poetry_classes import Limerick


def make_limerick(ngram):
    limerick = Limerick(ngram)
    starting_words = ngram.get_starting_words()
    limerick.build_full_limerick(starting_words)
    #limerick.print_limerick()
    limerick.evalutate()
    return limerick

def make_top_limericks(ngram):
    min_fitness = 2000
    top_limericks = []
    for number in range(5):
        limerick = make_limerick(ngram)
        top_limericks.append(limerick)
        if limerick.fitness < min_fitness:
            min_fitness = limerick.fitness
    return top_limericks, min_fitness

def get_limericks_above_100(ngram):
    top_limericks = []
    while len(top_limericks) < 3:
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


def get_poems(ngram):
    top_limericks, min_fitness = make_top_limericks(ngram)
    for num in range(50):
        limerick = make_limerick(ngram)
        if limerick.fitness > min_fitness:
            new_min = limerick.fitness
            for i in range(5):
                fit_num = top_limericks[i].fitness
                if(fit_num == min_fitness):
                    top_limericks[i] = limerick
                if(fit_num < new_min):
                    new_min = fit_num
            min_fitness = new_min 
    return top_limericks
        


def main():
    text = fr.read_file()
    ngram = fr.make_n_gram(text)
    #top_poems = get_poems(ngram)
    top_poems = get_limericks_above_100(ngram)
    print("_________________________________________")
    for poem in top_poems:
        print("_________________")
        print(poem.get_poem_name())
        poem.print_limerick()
        print(poem.fitness)
        print("_________________")

if __name__ == "__main__":
    main()

