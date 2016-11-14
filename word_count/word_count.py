#!/usr/bin/env python3


def words(n):
    word_c = {}
    for w in n.split():
        word_c[w] = word_c.get(w, 0) + 1
    return(word_c)
