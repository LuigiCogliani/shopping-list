import streamlit as st
import pandas as pd
from PIL import Image


def shopping_list(list_of_dishes):
    # print dishes selected
    st.subheader("Dishes")
    for dish in list_of_dishes:
        st.write(dish)
    # print shopping list
    st.subheader("Shopping List")
    for line in text.splitlines():
        st.write(line)


# streamlit wide layout
st.set_page_config(layout="wide")

# add page title
st.title(" Gousto Grocery List Generator")

# add hedaer
st.header("scroll recipes")

# initialise ingredients and recipes list
df = pd.read_csv("./data/Gousto_DB - Sheet1.csv")

# st.write(df.columns)


filter = st.sidebar.multiselect("Choose recipies", df["name"].unique())
df_ = df[df["name"].isin(filter)]
df_ = df_.groupby("ing_name", as_index=False)["ing_q"].sum()

# add generate button
button_generate_shopping_list = st.sidebar.button("Generate!")


text = df_.to_string(header=False, index=False, justify="left")

if button_generate_shopping_list:
    shopping_list(list_of_dishes=filter)
else:
    for id in df["id"].unique():
        try:
            image = Image.open("./data/01 pic/" + str(id) + ".jpg")
            st.image(image, caption=str(df.loc[df["id"] == id]["name"].unique()))
        except:
            pass
