import time
from Radix_Project.parsing.extraction import parsing_documents, RegxSections, RegxInfos, create_corpus
from Radix_Project.matching.tf_idf_embeddings import tf_idf_func
from sklearn.metrics.pairwise import linear_kernel
import joblib

documents = parsing_documents(3266, RegxSections, RegxInfos)

#corpus = joblib.load('resources/corpus.pkl')

# tf_idf_corpus_char = tf_idf_func(corpus, 'char')
# tf_idf_corpus_char_wb = tf_idf_func(corpus, 'char_wb')
# tf_idf_corpus_word = tf_idf_func(corpus, 'word')

#joblib.dump(documents, 'resources/documents_sample_v2.pkl')

#joblib.dump(documents, 'resources/documents_full_v3.pkl')
# joblib.dump(corpus, 'corpus.pkl')
