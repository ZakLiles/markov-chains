"""Generate Markov text from text files."""

from random import choice
from pprint import pprint as pp

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path) as file:
        contents = file.read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):

        word_pair = (words[i], words[i+1])
        next_word = words[i+2]
        
        if word_pair in chains:
            chains[word_pair].append(next_word)
        else:
            chains[word_pair] = [next_word]
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    key = choice(list(chains))
    words.extend(list(key))
    next_word = choice(chains[key])

    words.append(next_word)
    link = list(key)
    link.append(next_word)

    
    while tuple(link[1:]) in chains:
        next_word = choice(chains[tuple(link[1:])])
        words.append(next_word)
        link = link[1:]
        link.append(next_word)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
