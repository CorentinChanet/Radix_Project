import time
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from flair.embeddings import TransformerDocumentEmbeddings
from flair.data import Sentence
from enum import Enum
import nltk


# https://github.com/manishiitg/recruitai
# models_names = ['manishiitg/distilbert-resume-parts-classify']
# models_names = ['distilroberta-base']


def embed_func(models_names:list, documents:dict) -> dict:
    for model in models_names:
        embedding = TransformerDocumentEmbeddings(model)
        for i in range(1,len(documents)+1,1):
            if documents[i]:
                    documents[i][model] = {}
                    for key in documents[i]['sections'].keys():
                        text = " ".join(documents[i]['sections'][key])
                        if text:
                            sentence = Sentence(text)
                            embedding.embed(sentence)
                            documents[i][model][key] = sentence
                        else:
                            documents[i][model][key] = ""

    return documents

def sections_similarity(model_name:str, documents: dict) -> dict:
    all_results = {}
    for i in documents.keys():
        all_results[i] = {}
        for section in documents[i][model_name].keys():
            if documents[i][model_name][section]:
                all_results[i][section] = {}
                j = 1
                while j <= len(documents):
                    if j!= i and documents[j][model_name][section]:
                        all_results[i][section][j] = cosine_similarity(
                            documents[i][model_name][section].embedding.detach().numpy().reshape(1, -1),
                            documents[j][model_name][section].embedding.detach().numpy().reshape(1, -1)
                        )
                    j += 1

    return all_results