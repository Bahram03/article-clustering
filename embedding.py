import pandas as pd
import numpy as np
import csv
import pickle
from gensim.models import Word2Vec


def get_article_keywords():
  with open('articles.csv', 'r', encoding='utf-8') as file:
      reader = csv.reader(file)

      # Skip the header row
      next(reader)

      # Initialize an empty list to store keywords
      keywords_list = []

      # Iterate over each row in the CSV file
      for row in reader:
        # Extract the keywords column (index 5)
        keywords = row[4]

        # Split the keywords string by comma and remove whitespace
        keywords_array = [keyword.strip() for keyword in keywords.split(',')]

        # Append the keywords array to the list
        keywords_list.append(keywords_array)
      return keywords_list

def get_article_title():
  titles = pd.read_csv(r'titles.csv', encoding='utf-8')
  tokenized_texts = [eval(row) if isinstance(row, str) else row for row in titles['Title']]
  return tokenized_texts

def get_embeddings(model, keywords_list):
  # for each list of words we are going to generate a embedding vector
  embeddings = []
  for keyword in keywords_list:
      document_embedding = np.array([model.wv[word] for word in keyword if word in model.wv])
      # now we use the mean of all the words to represent each article
      average_vector = np.mean(document_embedding, axis=0)
      embeddings.append(average_vector)
  # make it a numpy array to later save it with pickle
  embeddings_array = np.array(embeddings)
  return embeddings_array

def load_pickle_object(name):
  with open(name, 'rb') as file:
    data = pickle.load(file)

  return data

def save_pickle_object(array, name):
  # Save embeddings tensor to file
  with open(name, "wb") as f:
    pickle.dump(array, f)


keywords_list = get_article_keywords()
word2vec_model_keywords = Word2Vec(sentences=keywords_list, vector_size=200, window=5, min_count=1, workers=4)
embeddings_keywords = get_embeddings(word2vec_model_keywords, keywords_list)
save_pickle_object(embeddings_keywords, 'keywords.pkl')


# create the embedding vectors for title to represent an article
title_list = load_pickle_object('assets/titles.pkl')
word2vec_model_titles = Word2Vec(sentences=title_list, vector_size=200, window=5, min_count=1, workers=4)
embeddings_titles = get_embeddings(word2vec_model_titles, title_list)
save_pickle_object(embeddings_titles, 'assets/titles.pkl')

