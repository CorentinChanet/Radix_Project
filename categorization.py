import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from flair.embeddings import TransformerDocumentEmbeddings
from flair.data import Sentence
from enum import Enum
import nltk
import time

class Patterns(Enum):
    work = r'(experience|employment|work|working|career|job.?|professional|previous).{0,4}(details|work|experience|background|highlight|summary|histor.{0,4}|position.?)|(experience|employment|career|job.?)'
    skill = r'(techn.{2,8}|)?.{0,4}(skill.?|qualification.?|knowledge)'

def get_sections(splitted_text, Patterns):
    res = []

    for chunck in splitted_text:
        pass


embedded_documents = []
#embedding = TransformerDocumentEmbeddings('distilroberta-base')
embedding = TransformerDocumentEmbeddings('manishiitg/distilbert-resume-parts-classify')

start = time.time()

for i in range(1,32,1):
    try:
        with open(f'../curriculum_vitae_data/pdf_to_txt/{i}.txt') as f:

            text = f.read()
            text.replace("\n", " ")

            sentence = Sentence(text)

            embedding.embed(sentence)

            embedded_documents.append(sentence)

    except:
        print(f"Could not find or embbed document {i}.txt")
        embedded_documents.append(False)

results = {}

print("==================")
middle = time.time()
print(middle - start)
print("==================")

for i, doc in enumerate(embedded_documents):
    results[i + 1] = {}
    if doc:
        j = 0
        while j < 31:
            if j != i:
                results[i + 1][j+1] = cosine_similarity(embedded_documents[i].embedding.detach().numpy().reshape(1, -1),
                                                      embedded_documents[j].embedding.detach().numpy().reshape(1, -1))
            j += 1


print("==================")
print(time.time() - middle)
print("==================")
print("==================")
print("Total: "+ str(time.time() - start))
print("==================")

# cosine_similarity(embedded_documents[3].embedding.detach().numpy().reshape(1, -1), embedded_documents[4].embedding.detach().numpy().reshape(1, -1))