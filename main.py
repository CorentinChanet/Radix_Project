# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

from pdfminer.high_level import extract_text
# from flair.data import Sentence
# from flair.models import SequenceTagger
import re


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


raw_text = extract_text_from_pdf('../curriculum_vitae_data/pdf/133.pdf')
split_text = re.split('\n', raw_text)
