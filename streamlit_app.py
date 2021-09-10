import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import joblib


st.set_page_config(layout="wide")
expander_extracting = st.expander("Information Extraction", expanded=False)

with expander_extracting:

    documents = joblib.load("resources/documents.pkl")
    documents_sample = joblib.load("resources/documents_sample.pkl")

    ee_0_left, ee_0_center, ee_0_right = st.columns((0.1, 1, 2))

    doc_index = ee_0_center.document_number = st.number_input("Resume number", min_value=1, max_value=3266, key='document_number_extraction')

    warning, _ = st.columns((1, 1))
    if not documents[doc_index]:
        warning.write("This document was removed from the dataset")

    ee_0_box_1, ee_0_box_2, ee_0_box_3, ee_0_box_4 = st.columns((1,1,1,1))

    tickbox_1 = ee_0_box_1.checkbox('Name', value=False)
    tickbox_2 = ee_0_box_2.checkbox('Email', value=False)
    tickbox_3 = ee_0_box_3.checkbox('Phone', value=False)
    tickbox_4 = ee_0_box_4.checkbox('Curriculum [< 100]')

    if tickbox_1 and documents[doc_index]['infos']['name']:
        ee_0_box_1.write(documents[doc_index]['infos']['name'])

    if tickbox_2 and documents[doc_index]['infos']['email_addresses']:
        ee_0_box_2.write([documents[doc_index]['infos']['email_addresses'][0]])

    if tickbox_3 and documents[doc_index]['infos']['phone_numbers']:
        ee_0_box_3.write([documents[doc_index]['infos']['phone_numbers'][0]])

    if tickbox_4 and documents_sample[doc_index]['infos']['curriculum']:
        ee_0_box_3.write(documents_sample[doc_index]['infos']['curriculum'])

    ee_1_box_5, ee_1_box_6, ee_1_box_7, ee_1_box_8 = st.columns((1,1,1,1))

    tickbox_5 = ee_1_box_5.checkbox('Education Section', value=False)
    tickbox_6 = ee_1_box_6.checkbox('Working Experience Section', value=False)
    tickbox_7 = ee_1_box_7.checkbox('Skills Section', value=False)
    tickbox_8 = ee_1_box_8.checkbox('Hobbies Section', value=False)

    if tickbox_5 and documents[doc_index]['sections']['education']:
        ee_1_box_5.write(documents[doc_index]['sections']['education'])

    if tickbox_6 and documents[doc_index]['sections']['work_exp']:
        ee_1_box_6.write(documents[doc_index]['sections']['work_exp'])

    if tickbox_7 and documents[doc_index]['sections']['skills']:
        ee_1_box_7.write(documents[doc_index]['sections']['skills'])

    if tickbox_8 and documents[doc_index]['sections']['hobbies']:
        ee_1_box_8.write(documents[doc_index]['sections']['hobbies'])

expander_matching = st.expander("Resume matching (from dataset)", expanded=False)

with expander_matching:

    em_0_left, em_0_center, em_0_right, em_0_padding = st.columns((1, 1, 1, 1))

    with em_0_left:
        section = st.selectbox("Select Section", ('work_exp',
                                                  'education',
                                                  'skills'))
    with em_0_center:
        document_number = st.number_input("Resume number", min_value=1, max_value=3266, key='document_number_matching')

    with em_0_right:
        vectorizer = st.selectbox("Select Vectorizer", ('char',
                                                  'word'))

    with em_0_left:
        search = st.checkbox('Search')

    em_1_left, em_1_center, em_1_right = st.columns((0.2, 1, 1))

    if search:
        tf_idf_corpus = joblib.load(f"resources/tf_idf_corpus_{vectorizer}.pkl")

        slider = em_0_center.slider("Choose which resume to compare", min_value=0, max_value=9, value=0)

        if tf_idf_corpus[section][document_number-1]:

            cosine_similarities = linear_kernel(tf_idf_corpus[f'{section}_matrix'][document_number-1], tf_idf_corpus[f'{section}_matrix']).flatten()
            ranking = cosine_similarities.argsort()[:-12:-1][1:] + 1

            em_1_left.write(list(ranking))

            em_1_center.write(documents[document_number]['sections'][section])

            em_1_right.write(documents[ranking[slider]]['sections'][section])

        else:
            em_1_left.write("No section found")

expander_matching_external = st.expander("Resume matching (upload file)", expanded=False)

with expander_matching_external:

    em_0_left, em_0_center, em_0_right, em_0_padding = st.columns((1, 1, 1, 1))

    with em_0_left:
        section_ext = st.selectbox("Select Section", ('work_exp',
                                                  'education',
                                                  'skills'), key="Select Section external")
    with em_0_center:
        document_ext = st.file_uploader('Drop your pdf file here', type='.pdf', key="Drop external")

    with em_0_right:
        vectorizer = st.selectbox("Select Vectorizer", ('char',
                                                  'word'), key='Vectorizer external')

    with em_0_left:
        search_ext = st.checkbox('Search', key="Search external")

    em_1_left, em_1_center, em_1_right = st.columns((0.2, 1, 1))

    if search:
        tf_idf_corpus = joblib.load(f"resources/tf_idf_corpus_{vectorizer}.pkl")