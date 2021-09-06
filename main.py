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

from parsing.extraction import parsing_documents, RegxSections, RegxInfos, create_corpus
from matching.tf_idf_embeddings import tf_idf_func
from sklearn.metrics.pairwise import linear_kernel
import re

documents = parsing_documents(3266, RegxSections, RegxInfos)

corpus = create_corpus(documents)

tf_idf_corpus = tf_idf_func(corpus)

cosine_similarities = linear_kernel(tf_idf_corpus['work_exp_matrix'][24:25], tf_idf_corpus['work_exp_matrix']).flatten()
indices = cosine_similarities.argsort()[:-5:-1]

print(time.time()-start)
#print(sorted(list(results[24]['education'].items()), key=lambda x: x[1]))