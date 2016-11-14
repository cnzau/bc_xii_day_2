#!/usr/bin/env python3
def words(sentence):
    """
    Given a string. This returns word count in a dictionary
    """
    word_return = {}
    for w in sentence.split():
        if w.isdigit():
            w = int(w)
            word_return[w] = word_return.get(w, 0) + 1
        else:
            if not w.isdigit():
                word_return[w] = word_return.get(w, 0) + 1
    return word_return
