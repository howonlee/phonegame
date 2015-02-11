import nltk
import random
from nltk.corpus import brown

if __name__ == "__main__":
    print "loading...."
    words = brown.tagged_words(tagset="universal")
    nouns = []
    for word, tag in words:
        if tag == "NOUN":
            nouns.append(word)
    while raw_input("-->") is not "q":
        print random.choice(nouns), random.choice(nouns)
