from flair.models import SequenceTagger
from flair.data import Sentence

with open(f'../../curriculum_vitae_data/pdf_to_txt/1.txt') as f:
    s = f.read()[:500]

tagger_full = SequenceTagger.load('flair/ner-english-ontonotes-large')
#tagger_default = SequenceTagger.load('ner')

sentence = Sentence(s)

tagger_full.predict(sentence)

print(sentence.to_tagged_string())


# str(sentence.to_dict(tag_type='ner')['entities'][0]['labels'][0]).split()