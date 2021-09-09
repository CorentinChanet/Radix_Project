# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

import time

start = time.time()

from Radix_Project.parsing.extraction import parsing_documents, RegxSections, RegxInfos, create_corpus
from Radix_Project.parsing.flair_ner import _extract_persons, _extract_edu
from Radix_Project.matching.tf_idf_embeddings import tf_idf_func
from sklearn.metrics.pairwise import linear_kernel
import joblib
import json
from Radix_Project.utils.json_encoder import NpEncoder

documents = parsing_documents(3266, RegxSections, RegxInfos)

corpus = joblib.load('resources/corpus.pkl')

# tf_idf_corpus_char = tf_idf_func(corpus, 'char')
# tf_idf_corpus_char_wb = tf_idf_func(corpus, 'char_wb')
tf_idf_corpus_word = tf_idf_func(corpus, 'word')

joblib.dump(tf_idf_corpus_word, 'resources/tf_idf_corpus_word.pkl')
print("Finished vectorization")

# sections_list = ['work_exp']
#
# char_ordering = {section: [] for section in sections_list}
# char_wb_ordering = {section: [] for section in sections_list}
# word_ordering = {section: [] for section in sections_list}
#
# for section in sections_list:
#
#     for i in range(0,3266,1):
#         cosine_similarities_char = linear_kernel(tf_idf_corpus_char[f'{section}_matrix'][i], tf_idf_corpus_char[f'{section}_matrix']).flatten()
#         cosine_similarities_char_wb = linear_kernel(tf_idf_corpus_char_wb[f'{section}_matrix'][i], tf_idf_corpus_char_wb[f'{section}_matrix']).flatten()
#         cosine_similarities_word = linear_kernel(tf_idf_corpus_word[f'{section}_matrix'][i], tf_idf_corpus_word[f'{section}_matrix']).flatten()
#
#         char_ordering[section].append((list(cosine_similarities_char.argsort()[:-101:-1]), sorted(cosine_similarities_char)[:-101:-1]))
#         char_wb_ordering[section].append((list(cosine_similarities_char_wb.argsort()[:-101:-1]), sorted(cosine_similarities_char_wb)[:-101:-1]))
#         word_ordering[section].append((list(cosine_similarities_word.argsort()[:-101:-1]), sorted(cosine_similarities_word)[:-101:-1]))
#         print(f'Document {i+1} processed')
#
#     with open('char_ordering.json', 'w') as file:
#         json.dump(char_ordering, file, cls=NpEncoder)
#     with open('char_wb_ordering.json', 'w') as file:
#         json.dump(char_wb_ordering, file, cls=NpEncoder)
#     with open('word_ordering.json', 'w') as file:
#         json.dump(word_ordering, file, cls=NpEncoder)
#     # joblib.dump(char_ordering[section], f'{section}_char_ordering.pkl')
#     # joblib.dump(char_wb__ordering[section], f'{section}_char_wb_ordering.pkl')
#     # joblib.dump(word_ordering[section], f'{section}_word_ordering.pkl')
#
#     print(f'{section} section pickled')
#
# joblib.dump(documents, 'documents.pkl')
# joblib.dump(corpus, 'corpus.pkl')

print(time.time()-start)