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
    print "loaded"
    while raw_input("--> ").lower() not in ["q", "quit", "exit"]:
        print random.choice(nouns), random.choice(nouns)
