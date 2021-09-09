import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import joblib


st.set_page_config(layout="wide")
expander_extracting = st.expander("Information Extraction", expanded=False)

with expander_extracting:

    ee_0_left, ee_0_center, ee_0_right = st.columns((0.1, 1, 0.1))

expander_matching = st.expander("Resume matching (from dataset)", expanded=False)

with expander_matching:

    em_0_left, em_0_center, em_0_right = st.columns((1, 1, 1))

    with em_0_left:
        section = st.selectbox("Select Section", ('work_exp',
                                                  'education',
                                                  'skills'))
    with em_0_center:
        document_number = st.number_input("Resume number", min_value=1, max_value=3266)

    with em_0_right:
        search = st.button('Search')

    if search:
        tf_idf_corpus = joblib.load(f"resources/tf_idf_corpus_word.pkl")
        if tf_idf_corpus[section][document_number-1]:
            cosine_similarities = linear_kernel(tf_idf_corpus[f'{section}_matrix'][document_number-1], tf_idf_corpus[f'{section}_matrix']).flatten()
            st.write(cosine_similarities.argsort()[:-13:-1][1:])
        else:
            st.write("No section found")

expander_matching_external = st.expander("Resume matching (upload file)", expanded=False)

with expander_matching_external:

    em_0_left, em_0_center, em_0_right = st.columns((1, 1, 1))

    with em_0_left:
        section_ext = st.selectbox("Select Section", ('work_exp',
                                                  'education',
                                                  'skills'), key="Select Section external")
    with em_0_center:
        document_ext = st.file_uploader('Drop your pdf file here', type='.pdf', key="Drop external")

    with em_0_right:
        search_ext = st.button('Search', key="Search external")

    if search:
        pass