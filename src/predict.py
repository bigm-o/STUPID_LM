import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import pickle

filename1 = './models/NB_model.pkl'
filename2 = './models/vectorizer.pkl'

NB_model = pickle.load(open(filename1, 'rb'))
vectorizer = pickle.load(open(filename2, 'rb'))

def predict_word(input, model = NB_model):
    input_df = pd.Series(str(input))

    # Transform the input text using the same vectorizer
    new_review = vectorizer.transform(input_df)
    # Get class probabilities
    proba = model.predict_proba(new_review)

    # Get top 5 classes for each sample
    top_k = 5
    top_classes = np.argsort(proba, axis=1)[:, -top_k:][:, ::-1]  # sort and reverse

    # Map to class labels
    top_class_labels = model.classes_[top_classes][0]
    rand_variable = random.choice(top_class_labels)

    return rand_variable


def generate_sentence(words, word_count = 50, model = NB_model):
    word_list = words.split(" ")  # turn input into list of words

    for n in range(word_count):
        main_words = ' '.join(word_list)  # form the current context string
        next_word = str(predict_word(main_words, model))  # predict the next word
        words = words + " " + next_word  # add it to the sentence
        word_list = word_list[1:]  # shift the context window
        word_list.append(next_word)  # include the new word

    return words


print(generate_sentence("video games work best with"))
