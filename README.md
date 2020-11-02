# Poetry_Slam
CSCI 3725 Mission 6: Create a poetry generation and evaluation system.

This system creates limericks inspired from Bob Ross's season 28 youtube transcripts that are then evaluated and eventually displayed on the brouser. This program utilizes n-grams, parse trees as well as other characteristics of limericks and topics we have discussed in class. I have named my program LACTIC - Limericks Accessed Creatively Through Intentional Computation.

## file_reader.py
This file reads in the Bob Ross script files and creates the ngram object. It does so by utilizing the functions **read_file** and **make_n_gram**. This is an essential aspect of this program because it is the way the 'inspiring set' is built and put into a useful data structure.

## make_html.py
This file This file contains the functions to create and write to an html file that will display and read aloud each given poem. The functions **make_html_doc** and **html_text** utilize information from a given poem in order to write appropriately to the produced file, but also name the resulting files as well. This is an important aspect of the program in relationship to the human interaction with the resulting poetry.

## n_gram.py
This file contains the n_gram class and all of it's associated functions. In this case it is a bigram, and this class offers the appropriate access to information. Other classes are able to retrive words based on probabilities and specifications, as well as add to the bigram, through the functions **add_to_ngram**, **retreive_next_word**, **retreive_ryming_word**, and **get_starting_words**. Without this file, there would be no logic to the process of production of the limericks.

## poetry_classes.py
This file contains the limerick class and all of it's associated functions. This class is essentail for the functionality of creating ("writing"), evaluating and naming the poems. The evaluation of poems is processed through a parse tree. Functions that support the creation of poems are **get_syllables**, **build_first_or_third**, **build_other_lines**, **build_full_limerick**, **get_noun**, **get_adj**, **get_noun_list**, **get_adj_list**, and **get_poem_name**. Functions that support the evalutation process are **evalutate**, **evaluate_lines**, **evaluate_rhyme**, **examine_line**, **compare_tag**, and **get_tags**. This file is essential to the creation of LACTIC's poetry.

## poetry_generator.py
This file drives the poetry generation process, and includes our main function. This is where limericks and their files are actually made by calling uppon the other files and consolodating their functions. Limericks are made through the **make_limerick** function, and **get_limericks_above_100** uses it to create the list of quality limericks. **create_files** creates the html files. **main** runs the entire program.

## Running the program
To run the program, first clone this github repository onto your local machine in a directory of your choice.

git clone [link to this repo]
Then, simply run the following command from the terminal in the Poetry_Slam directory:

python3 poetry_generator.py

```bash
python3 poetry_generator.py
```

Once the program has run, access the poem files in the poems folder and double click the file in order to open it in your browser. 

## Scholarly Sources


## Referenced Resources
- https://www.youtube.com/watch?v=VAkquAxQUPc
- https://spacy.io/usage/spacy-101#whats-spacy
- https://www.nltk.org/book/ch08.html
- https://universaldependencies.org/docs/u/pos/
- https://pronouncing.readthedocs.io/en/latest/tutorial.html#next-steps
- https://pronouncing.readthedocs.io/en/latest/tutorial.html#
- 
