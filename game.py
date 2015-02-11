import nltk
import random
from nltk.corpus import brown

if __name__ == "__main__":
    words = brown.tagged_words()
    nouns = []
    for word, tag in words:
        if tag == "NN":
            nouns.append(word)
    print random.choice(nouns), random.choice(nouns)
