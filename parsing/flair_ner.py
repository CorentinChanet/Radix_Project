from flair.data import Sentence
import joblib


def _extract_persons(text, tagger):

    text = " ".join(text.strip().split()[:30])

    sentence = Sentence(text)

    tagger.predict(sentence)

    names = []
    name_parts = []

    chunks = sentence.to_tagged_string().split()

    for i, chunk in enumerate(chunks):
        if '<S-PERSON>' in chunk:
            names.append(chunks[i - 1])
        elif '<B-PERSON>' in chunk or '<M-PERSON>' in chunk:
            name_parts.append(chunks[i-1])
        elif '<E-PERSON>' in chunk:
            name_parts.append(chunks[i - 1])
            names.append(" ".join(name_parts))
            name_parts = []

    return names

def _extract_work(section, tagger):

    dates = []

    for sent in section:

        sentence = Sentence(sent)

        tagger.predict(sentence)


        date_parts = []

        chunks = sentence.to_tagged_string().split()

        for i, chunk in enumerate(chunks):
            if '<S-DATE>' in chunk:
                dates.append(chunks[i - 1])
            elif '<B-DATE>' in chunk or '<M-DATE>' in chunk:
                date_parts.append(chunks[i-1])
            elif '<E-DATE>' in chunk:
                date_parts.append(chunks[i - 1])
                dates.append(" ".join(date_parts))
                date_parts = []

    return dates


# str(sentence.to_dict(tag_type='ner')['entities'][0]['labels'][0]).split()