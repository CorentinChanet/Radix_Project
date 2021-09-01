import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from flair.embeddings import TransformerDocumentEmbeddings
from flair.data import Sentence
from enum import Enum
import nltk
import time

# https://github.com/manishiitg/recruitai
models_names = ['manishiitg/distilbert-resume-parts-classify']
# models_names = ['distilroberta-base']


def embed_func(models_names:list, n_range:int) -> dict:

    embedded_documents_by_model = {}
    #embedding = TransformerDocumentEmbeddings('distilroberta-base')

    for model in models_names:
        embedding = TransformerDocumentEmbeddings(model)
        embedded_documents_by_model[model] = []

        for i in range(1,n_range,1):
            try:
                with open(f'../../curriculum_vitae_data/pdf_to_txt/{i}.txt') as f:

                    text = f.read()
                    text.replace("\n", " ")

                    sentence = Sentence(text)

                    embedding.embed(sentence)

                    embedded_documents_by_model[model].append(sentence)

            except:
                print(f"Could not find or embbed document {i}.txt")
                embedded_documents_by_model[model].append(False)

        return embedded_documents_by_model

def similarity_func(embedded_documents_by_model: dict) -> dict:
    all_results = {}
    for model in embedded_documents_by_model.keys():
        embedded_documents = embedded_documents_by_model[model]
        all_results[model] = {}
        model_results = {}
        for i, doc in enumerate(embedded_documents):
            model_results[i + 1] = {}
            if doc:
                j = 0
                while j < 31:
                    if j != i:
                        model_results[i + 1][j+1] = cosine_similarity(embedded_documents[i].embedding.detach().numpy().reshape(1, -1),
                                                              embedded_documents[j].embedding.detach().numpy().reshape(1, -1))
                    j += 1
    return all_results


for i in range(501,601,1):
    try :
        with open(f'../../curriculum_vitae_data/pdf_to_txt/{i}.txt') as f:
            txt = f.read()
    except:
        continue

    split_text = re.split('\n', txt)

    for sentence in split_text:
        if re.findall(r'((experience|employment|work|working|career|job.?|professional|previous).{0,3}(details|work|experience|overview|background|highlight|summary|histor.{0,4}|position.?))', sentence.lower()) or \
                re.findall(r"^experience.{0,2}$|^achievement.{0,2}$|^career.{0,2}$|^job.{0,2}$", sentence.lower().strip()):
            print(f"---{i}---")
            print(sentence)
            print(f"-------")