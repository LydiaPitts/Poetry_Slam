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

def update_top_limericks(top_limericks, limerick, min_fitness):
    replace = False
    index_to_replace = 0
    if limerick.fitness > min_fitness:
        print("in loop. Min fitness:", min_fitness, " Compare_fitness ", limerick.fitness)
        new_min = limerick.fitness
        for i in range(5):
            fit_num = top_limericks[i].fitness
            print("Item in array num: ", fit_num, " New_fitness, ", limerick.fitness)
            if(fit_num == min_fitness):
                print("Replace this")
                replace = True
                index_to_replace = i
                #top_limericks[i] = limerick
            if(fit_num < new_min):
                new_min = fit_num
            if(limerick.first_line == top_limericks[i].first_line):
                print("found same poem")
                return top_limericks
            min_fitness = new_min
    if(replace):
        top_limericks[index_to_replace] = limerick
        print("YAY")
    return top_limericks, min_fitness


def get_poems(ngram):
    top_limericks, min_fitness = make_top_limericks(ngram)
    #print(min_fitness)
    for num in range(50):
        limerick = make_limerick(ngram)
        #top_limericks, min_fitness = update_top_limericks(top_limericks, limerick, min_fitness)
        #replace = false
       # replace_index = 0
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
    top_poems = get_poems(ngram)
    print("_________________________________________")
    for poem in top_poems:
        print("_________________")
        print(poem.get_poem_name())
        poem.print_limerick()
        print(poem.fitness)
        print("_________________")

if __name__ == "__main__":
    main()

