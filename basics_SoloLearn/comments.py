# -*- coding: utf-8 -*-


#.....................................................

#comment: number of days in a year
d=365
#comment: number of months i a year
m=12

print(d/m) #average number of days in a month

#.....................................................

def shout(word):
    """
    Print a word with an exclamation mark

    Parameters
    ----------
    word : string
        Word to be shouted.

    Returns
    -------
    The shouted word.

    """
    return word + "!!!!!!"

shout("Basta")
