from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def summarize(text):
  sentences = text.split(".")
  vectorizer = TfidfVectorizer(stop_words="english")
  tfidf_matrix = vectorizer.fit_transform(sentences)
  # Compute similarity matrix
  cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
  # Rank sentences based on their similarity
  sentence_scores = cosine_similarities.sum(axis=1)
  ranked_sentences = [sentences[i] for i in np.argsort(sentence_scores)[::-1]]
  # Select top 2 sentences for summarization
  summary = " ".join(ranked_sentences[:2])
  return summary
#this is trial module
