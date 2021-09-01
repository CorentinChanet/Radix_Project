import fitz
import re
import os


for i in range(1, 3267, 1):

    try:
        doc = fitz.Document(f'../../curriculum_vitae_data/pdf/{i}.pdf')
        f = open(f'../../curriculum_vitae_data/pdf_to_txt/{i}.txt', 'w')
        f.close()

        for page in range(doc.page_count):
            page = doc.load_page(page)
            raw_text = page.get_textpage('words').extractText()
            raw_text = re.sub(r"\n:", r":", raw_text)

            f = open(f'../../curriculum_vitae_data/pdf_to_txt/{i}.txt', 'a+')
            f.write(raw_text)
            f.close()

    except:
        print(f"Could not find/process {i}.pdf")


