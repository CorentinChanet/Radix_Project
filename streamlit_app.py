import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import tkinter as tk
from tkinter import filedialog
from io import StringIO


st.title('Radix Matching')

#Here we will upload a file

st.write('Upload the resume you want to match')
uploaded_file = st.file_uploader("")
if uploaded_file is not None:
     # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

     # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

     # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    #dataframe = pd.read_csv(uploaded_file)
    #st.write(dataframe)

#Here i ll try to mark