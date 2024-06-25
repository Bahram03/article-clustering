from hazm import Normalizer, WordTokenizer, POSTagger, Stemmer, Lemmatizer
import pandas as pd
import csv
import pickle


def is_useful(tag):
    return tag not in {'PUNCT', 'NUM', 'ADP', 'ADV', 'DET', 'INTJ', 'ADP,EZ', 'DET,EZ', 'SCONJ',
                       'VERB', 'PRON', 'CCONJ', 'NUM,EZ', 'PRON,EZ', 'ADV,EZ', 'CCONJ,EZ'}


titles = list()

with open('assets/articles.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        # abstracts are stored in the forth column
        titles.append(row[3])


normalizer = Normalizer()
tokenizer = WordTokenizer()
stemmer = Stemmer()
tagger = POSTagger(model='assets/pos_tagger.model')

normalized_titles = [normalizer.normalize(title) for title in titles]
tokenized_titles = [tokenizer.tokenize(title) for title in normalized_titles]
stemmed_titles = [[stemmer.stem(word) for word in words] for words in tokenized_titles]
cleaned_titles = list()
broken_articles_index = list()
for i, stemmed in enumerate(stemmed_titles):
    tagged = tagger.tag(stemmed)
    temp_title = list()
    for tagged_word in tagged:
        if is_useful(tagged_word[1]):
            temp_title.append(tagged_word[0])
    cleaned_titles.append(temp_title)


with open('assets/titles.pkl', 'wb') as file:
    pickle.dump(cleaned_titles, file)

