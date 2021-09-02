import re
from enum import Enum
import time
import joblib

class Sections(Enum):
    work = r'((teaching|exp.{3,4}nce|employment|work|working|career|job.?|professional|organizational|industr.{1,3}|previous.{0,2}|present.{0,2}|current.{0,2}|detail.{0,2})' \
           r'.{0,4}' \
           r'(record.?|role.?|responsibilit.{1,4}|exposure|synopsis|detail.?|exp.{3,4}nce|employ.{2,4}|overview|background|highlight|summar.{1,3}|histor.{0,4}|position.?)' \
           r'|^.{0,6}internship|^.{0,6}experience|^.{0,6}career.{0,4}$|^.{0,6}job.{0,5}$|^personal experience$|^.{0,6}responsibilit.{1,6}$|^.{0,6}dut.{1,3})'
    education = r'(school.{0,5}|schola.{1,5}|project.?|vocation.{1,4}|academi.{1,4}|education.{0,4}|university|college|high school|graduat.{1,4}).{0,4}(training.?|qualifi.{2,9}|detail.?|purview|project.?|record.?|overview|training|background|highlight|summar.{1,3}|histor.{0,4}|achievement.?|course.?|credential.?|profile)|^education.{0,5}$|^certificat.{1,4}|^qualifi.{1,6}$|professional qualifi.{2,9}|professional training|^schola.{1,5}$|^.{0,6}achievement.{0,5}$|additional qualific|academi.{1,4}'
    skills = r'(techn.{2,8}|core|key|area.?|professional|additional|organization.{0,2}|software|it|industry|personal.{0,3}|computer|relevant|hard.{0,5}|soft).{0,4}(skil.{1,2}|trait.?|knowledge|strength.?|proficiency|competenc.{1,4}|capabilit.{1,4}|capacit.{1,4}|experti.e|literacy)|^skill.{0,4}|^strength.{0,4}'
    personal = r'(person.{0,2}|contact|about|identity|passport).{0,4}(detail.?|info.{0,9}|profile)|^information$|address'


def _get_sections(text, regexes):
    sections = {pattern.name:[] for pattern in regexes}
    split_text = re.split('\n', text)
    current_section = ""
    for sentence in split_text:
        for pattern in regexes:
            if re.findall(pattern.value, sentence.lower().strip()) and current_section != pattern.name:
                current_section = pattern.name
                break

        if current_section:
            sections[current_section].append(sentence)

    return sections

def parsing_sections(n, regexes):
    documents = {i:{} for i in range(1,n+1,1)}
    for i in range(1,n+1,1):
        try :
            with open(f'../curriculum_vitae_data/pdf_to_txt/{i}.txt') as f:
                txt = f.read()
        except:
            documents[i] = False
            continue

        documents[i] = _get_sections(txt, regexes)

    return documents

start = time.time()
documents = parsing_sections(3266, Sections)

joblib.dump(documents, "documments.pkl")
print(time.time()-start)




