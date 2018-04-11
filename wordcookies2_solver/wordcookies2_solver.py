# -*- coding: utf-8 -*-
from nltk.corpus import words
from itertools import permutations


def wordlist(letter_string, length=None):
    """Generate list of english words formed from letters in letter string.
    
    Arguments:
        letter_string {str} -- String of all of the letters that can be used 
            to make the return words.
    
    Keyword Arguments:
        length {int} -- Length of the word in question. Can be used to limit 
            the return to words that fit in a certain spot. If no value is 
            provided all words are returned regardless of length. 
            (default: {None})
    
    Returns:
        list -- Returns a list of strings, each of which is an english word 
            comprised of the letters in letter_string.
    """

    # If the word list has been downloaded on computer, use it. Otherwise,
    # download it first, then use it.
    try:
        word_list = words.words()
    except LookupError:
        import nltk
        nltk.download('words')
        word_list = words.words()

    if length is None:
        l = len(letter_string)
        dim_list = [
            [''.join(i) for i in permutations(letter_string, j)] 
            for j 
            in range(3,l+1)
        ]
        flat_words = [item for sublist in dim_list for item in sublist]
    else:
        # only generate words of appropriate length
        flat_words = [''.join(i) for i in permutations(letter_string, length)]

    english_words = [w for w in word_list if w in flat_words]

    return english_words
