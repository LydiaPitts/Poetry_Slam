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
    limerick.print_limerick()
    limerick.evalutate()
    return limerick

def get_poems(ngram):
    min_fitness = 2000
    top_limericks = []
    for number in range(5):
        limerick = make_limerick(ngram)
        top_limericks.append(limerick)
        if limerick.fitness < min_fitness:
            min_fitness = limerick.fitness
    print(min_fitness)
    for num in range(7):
        limerick = make_limerick(ngram)
        if limerick.fitness > min_fitness:
            new_min = limerick.fitness
            for i in range(5):
                fit_num = top_limericks[i].fitness
                if(fit_num == min_fitness):
                    print("Limerick OG: ", top_limericks[i])
                    top_limericks[i] = limerick
                    print("Limerick New: ", top_limericks[i])
                if(fit_num < new_min):
                    new_min = fit_num
            min_fitness = new_min
            print("new fitness ", min_fitness)
    print("______________________________")
    for i in range(5):
        print(top_limericks[i].fitness)
    return top_limericks


        



def main():
    text = fr.read_file()
    ngram = fr.make_n_gram(text)
    top_poems = get_poems(ngram)

if __name__ == "__main__":
    main()

