import re
from enum import Enum
import joblib
from Radix_Project.parsing.flair_ner import _extract_persons, _extract_edu
tagger = joblib.load("../NLP-resume/processing/ner_onto_large.pkl")

class RegxSections(Enum):
    work_exp = r'((teaching|exp.{3,4}nce|employment|work|working|career|job.?|professional|organizational|industr.{1,3}|previous.{0,2}|present.{0,2}|current.{0,2}|detail.{0,2})' \
           r'.{0,4}' \
           r'(record.?|role.?|responsibilit.{1,4}|exposure|synopsis|detail.?|profile.?|exp.{3,4}nce|employ.{2,4}|overview|background|highlight|summar.{1,3}|histor.{0,4}|position.?|ap.?oint.?ment.?)' \
           r'|^.{0,6}internship|^.{0,6}experience|^.{0,6}career.{0,4}$|^.{0,6}job.{0,5}$|^.?personal experience$|^.{0,6}responsibilit.{1,6}$|^.{0,6}dut.{1,3}|^.?assig.{0,2}ment.?)'
    education = r'(school.{0,5}|schola.{1,5}|project.?|vocation.{1,4}|academi.{1,4}|education.{0,4}|university|college|high school|graduat.{1,4}|degree.?).{0,4}(training.?|qualifi.{2,9}|detail.?|purview|project.?|record.?|overview|training|background|highlight|summar.{1,3}|histor.{0,4}|course.?|credential.?|profile)|^.?education.{0,6}$|^.?certificat.{1,4}|^.?qualifi.{1,6}$|professional qualifi.{2,9}|professional training|^.?schola.{1,5}$|^.{0,6}achievement.{0,5}$|additional qualific|academi.{1,4}'
    skills = r'(techn.{2,8}|core|key|area.?|professional|additional|organization.{0,2}|software|it|industry|personal.{0,3}|computer|relevant|hard.{0,5}|soft|practical).{0,4}(skil.{1,35}$|trait.?|knowledge|strength.?|proficiency|competenc.{1,4}|capabilit.{1,4}|capacit.{1,4}|abilit.{1,4}|experti.e|literacy)|^.?skill.{0,4}|^.?strength.{0,4}|^.?proficienc.{1,3}'
    hobbies = r'(extra|activit.{1,4}).{0,12}(activit.{1,3})|^.?hobb.{1,3}|^.?activit.{1,4}'
    interests = r'(area.{0,1}|field.?).{0,4}(interest.{0,1})'
    personal_info = r'(person.{0,2}|contact|about|identity|passport).{0,4}(detail.?|info.{0,9}|profile|data)|^.?information$|address'
    declaration = r'^.?declaration'

class RegxInfos(Enum):
    email_addresses = r'[\w.+-]+@[\w-]+\.[\w.-]+'
    phone_numbers = r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3,4}[-\.\s]??\d{3,4}[-\.\s]??\d{4}|\(\d{3,4}\)\s*\d{3,4}[-\.\s]??\d{4}|\d{3,4}[-\.\s]??\d{4}))"

def _get_sections(text:str, regexes):
    sections = {pattern.name:[] for pattern in regexes}
    split_text = re.split('\n', text)
    current_section = ""
    for sentence in split_text:
        for pattern in regexes:
            if re.findall(pattern.value, sentence.lower().strip()) and current_section != pattern.name:
                current_section = pattern.name
                break

        if current_section:
            sentence = sentence.strip()
            if sentence and not sentence.isupper():
                sections[current_section].append(sentence)

    return sections

def _get_infos(text:str, regexes):
    infos = {pattern.name:[] for pattern in regexes}
    for pattern in regexes:
        matches = re.findall(pattern.value, text.lower())
        if matches:
            infos[pattern.name] = list(dict.fromkeys(matches)) # Removes any duplicate

    return infos

def _parse_name(text:str, tagger):
    return _extract_persons(text, tagger)

def parsing_documents(n, Sections, Infos):
    documents = {i:{} for i in range(1,n+1,1)}
    for i in range(1,n+1,1):
        try :
            with open(f'../curriculum_vitae_data/pdf_to_txt/{i}.txt') as f:
                txt = f.read()

        except:
            documents[i] = False
            continue

        documents[i]['sections'] = _get_sections(txt, Sections)
        documents[i]['infos'] = _get_infos(txt, Infos)
        # if documents[i]['sections']['education']:
        #     documents[i]['infos']['curriculum'] = _extract_edu(documents[i]['sections']['education'], tagger)
        # else:
        #     documents[i]['infos']['curriculum'] = []
        documents[i]['infos']['name'] = _extract_persons(txt, tagger)
        print(f'NER done on document {i}')

    return documents

def create_corpus(documents:dict):
    corpus = {pattern.name:[] for pattern in RegxSections}
    for i in range(1,len(documents)+1,1):
        if documents[i]:
            for section, content in documents[i]['sections'].items():
                if content:
                    text = " ".join(content)
                    corpus[section].append(text)
                else:
                    corpus[section].append("")
        else:
            for pattern in RegxSections:
                corpus[pattern.name].append("")

    return corpus
