#!/usr/bin/env python3
    
def word_count(sent):
  words = {}
  for w in sent.split():
    words[w] = words.get(w, 0) + 1
  for w, c in words.items():
    print("%s: %d" % (w, c))

word_count("olly Olly in  come free")
word_count("olly olly in  come free")
word_count('testing 1 2 testing')