import streamlit as st
import pandas as pd


st.write("""# Grocery List Generator""")

df = pd.read_csv('Shopping_list.csv')
with st.sidebar.form(key='my_form'):
    filter_ing = st.checkbox('Ingredients filter')
    if filter_ing:
        st.write("""# test""")
        #filter1 = st.multiselect('Choose recipies',df['name'].unique()) 
    filter = st.multiselect('Choose recipies',df['name'].unique()) 
    submit_button = st.form_submit_button(label='Generate!')
#filter = st.sidebar.multiselect('Choose recipies',df['name'].unique()) 
df_ = df[df['name'].isin(filter)]
df_ = df_.groupby('ing_name', as_index=False)['ing_q'].sum()

text = df_.to_string(header=False,index=False,justify='left')
if submit_button:
    for line in text.splitlines():
        st.checkbox(line)

