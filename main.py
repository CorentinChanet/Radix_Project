import docx2txt
import nltk
import re

from nltk.tokenize import word_tokenize, sent_tokenize

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')



filepath = 'word/1.docx'
# extract text
text = docx2txt.process(filepath)
#print(text)

#Remove every \t
if text:
    text = text.replace('\t','')

nolineBreaks = text.split('\n')
#print(nolineBreaks)
nospaces = []

for word in nolineBreaks:
    if word == "":
        pass
    else:
        nospaces.append(word)
print(nospaces)


def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None



def extract_text_names(txt):
    result = "('%s')" % "','".join(txt)
    return result

def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )
    return person_names

result = "('%s')" % "','".join(nospaces)
print(result)

import re
#COUCOU
name= r"name.?"
list1 = [name ,"VITAE"]
#Regex
#chercher fonction regex

text = "'Personal Information'.'CURRICULUM VITAE'.'Full Names: Mike Kisasati Wanaswa'.'ID Card No.22859930'.'Postal Address: P.O. Box 85575 80100 Mombasa'"
sentences_with_word = []
for sen in sent_tokenize(text):
    l = word_tokenize(sen)
    if len(set(l).intersection(list1))>0:
        sentences_with_word.append(sen)
print(sentences_with_word)

result = "('%s')" % "','".join(sentences_with_word)
if __name__ == '__main__':

    #text = extract_text_from_docx(filepath)
    names = extract_names(result)

    if names:
        print(names)
#regex



str1 = ''.join(str(e) for e in nospaces)


#print(str1)
#result = re.search("Names: (.*)ID", )
#print("Coucou "+result.group(1))