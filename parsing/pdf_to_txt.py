import fitz
import re


def convert_all():
    for i in range(1, 3267, 1):
        try:
            doc = fitz.Document(f'../../curriculum_vitae_data/pdf/{i}.pdf')
            f = open(f'../../curriculum_vitae_data/pdf_to_txt/{i}.txt', 'w')
            f.close()

            for page in range(doc.page_count):
                page = doc.load_page(page)
                raw_text = page.get_textpage('words').extractText()
                txt = re.sub(r"\n:", r":", raw_text)
                txt = re.sub(r'[^\x00-\x7F]+(\s)*', '', txt)
                txt = re.sub(r":([A-Z])", r": \1", txt)
                txt = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
                txt = re.sub(r'([A-Z]{3})([a-z])', r'\1 \2', txt)
                txt = re.sub(r'( )([a-z])( )', r'\2', txt)
                f = open(f'../../curriculum_vitae_data/pdf_to_txt/{i}.txt', 'a+')
                f.write(txt)
                f.close()

        except:
            print(f"Could not find/process {i}.pdf")


