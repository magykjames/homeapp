#!/usr/bin/python
from math import floor
from itertools import chain
from random import shuffle, randrange as rr
import string



def genrandom(length=None,
              upperletters=True,
              lowerletters=True,
              numbers=True,
              special=True,
              safe=False):
    # Generate sets of character types to choose from.
    lcl = list(string.ascii_lowercase)
    ucl = list(string.ascii_uppercase)
    numl = list(range(0, 10))
    specl = ['!', '@', '#', '$', '%', '^', '*', '(', ')']
    if safe is False:
        specl = [chr(x) for x in range(33, 127)
             if '\\' not in chr(x)
             and chr(x) not in [str(n) for n in numl]
             and chr(x) not in lcl and chr(x) not in ucl]

    # Populate pwordchoices based on which sets people want to use.
    pwordchoices = {}
    if upperletters:
        pwordchoices['1'] = ucl
    if lowerletters:
        pwordchoices['2'] = lcl
    if numbers:
        pwordchoices['3'] = numl
    if special:
        pwordchoices['4'] = specl

    # If user didn't choose any sets, use them all!
    if not pwordchoices:
        pwordchoices = {
            '1': lcl,
            '2': ucl,
            '3': numl,
            '4': specl}

    # totalopts will help is keep from repeating characters until we have to.
    totalopts = len(list(chain(*[pwordchoices[k] for k in pwordchoices.keys()])))
    # Number of opts will be used to define what sets are available.
    numopts = len(pwordchoices.keys())

    # Default password length to 6 chars if not specified.
    if not length or length < 6:
        length = 6
    # Function to pull a random item out of a (maybe) random set.
    def getchoice(x):
        # Make sure we at least cover one of each option.
        if x <= numopts:
            sel = pwordchoices.keys()[x - 1]
        else:
            # We have one of each, now just pick a random set.
            sel = pwordchoices.keys()[rr(0, numopts)]
        # Fetch the items from that set.
        choice = pwordchoices[str(sel)]
        # Pick a random item.
        return str(choice[rr(0, len(choice))])
    # Empty list to hold our password.
    pword = []
    # Start counting from 1 and keep looking for characters until meet the
    # length requirement.
    x = 1
    while x <= length:
        # c is the number of times we're allowed to repeat characters.
        c = int(floor(x / (totalopts + .5)))
        # Grab a random character (rc) from a (maybe) random set.
        rc = getchoice(x)
        # Check and make sure it isn't repeated more than c.
        if pword.count(rc) <= c:
            # If so add it, otherwise try again.
            pword.append(rc)
            # Mix it up since we might have had to use required sets.
            shuffle(pword)
            x += 1
    # Get the total unique characters in the password (set of password, sp).
    sp = list(set(pword))
    # Find out how many times we've had to repeat characters (rep).
    rep = [x for x in pword if pword.count(x) > 1]
    repstr = ', '.join(['{}*{}'.format(x, pword.count(x)) for x in set(rep)])
    # Do some silly stuff for grammer (character(s)) (ch)
    ch = ''
    if len(rep) == 0 or len(rep) > 1:
        ch = 's'
    # Generate a summary to be displayed in template/output.
    summary = '{} repeated character{}: [{}]'.format(
        (int(round(len(rep) / 2.0))), ch, repstr)
    # Make sure pword doesn't start with a leading 0, some PIN sites are picky.
    while pword[0] == '0':
        shuffle(pword)
    return (''.join(pword), summary)
