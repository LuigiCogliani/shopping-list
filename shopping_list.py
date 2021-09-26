import streamlit as st
import pandas as pd


st.write("""# Grocery List Generator""")

df = pd.read_csv('Shopping_list - Sheet2.csv')

filter_ing_check = st.sidebar.checkbox('Ingredients filter')
if filter_ing_check:
    filter_ing = st.sidebar.multiselect('Choose ingredients',df.sort_values('ing_name')['ing_name'].unique()) 
    
    filter = st.sidebar.multiselect('Choose recipies',df[df['ing_name'].isin(filter_ing)].sort_values('name')['name'].unique()) 
else:
    filter = st.sidebar.multiselect('Choose recipies',df.sort_values('name')['name'].unique()) 



df_ = df[df['name'].isin(filter)]
df_ = df_.groupby('ing_name', as_index=False)['ing_q'].sum()

text = df_.to_string(header=False,index=False,justify='left')

for line in text.splitlines():
   st.checkbox(line)

