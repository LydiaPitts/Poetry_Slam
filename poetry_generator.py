
import pronouncing
from collections import Counter
import nltk
from ngram_generator import Ngram


def main():





    '''
   print(pronouncing.phones_for_word("permit"))

   text = "wow like there are a lot of things going on"
   count = Counter()
   words = text.split()
   for word in words:
       pronunciation_list = pronouncing.phones_for_word(word)
       if len(pronunciation_list) > 0:
           count.update(pronunciation_list[0].split(" "))

   print(count.most_common(5))

   pronunciation_list = pronouncing.phones_for_word("whatever")
   print(pronouncing.syllable_count(pronunciation_list[0]))

   print(pronouncing.rhymes("failings"))'''

if __name__ == "__main__":
    main()
