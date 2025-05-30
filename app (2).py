# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19a6QVQq1uluspY5JSOBPdty5RBEN6mKe
"""

import streamlit as st
import pandas as pd

st.title("Job Listing Clusters")

df = pd.read_csv('clustered_jobs.csv')
clusters = df['cluster'].unique()

cluster_selected = st.sidebar.multiselect("Select clusters", clusters)

if cluster_selected:
    filtered = df[df['cluster'].isin(cluster_selected)]
    st.write(filtered)
else:
    st.write(df)