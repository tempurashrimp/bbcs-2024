import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='alhaitham', page_icon='🌿')
st.markdown("# Main page ")
st.sidebar.markdown("# Main page ")


st.markdown('# :rainbow[CHAT IS THIS REAL :fire: ]')
st.header('Is it over for me?')
st.image('https://pbs.twimg.com/media/FkFoeLhWIAAPYuQ?format=jpg&name=large')

st.markdown('*STUDENT DIET AND GPA*')
prompt = st.text_input(label='type student index here', value='20')

df = pd.read_csv('food_coded.csv')

try:
    st.write('GPA: ' + df.iloc[int(prompt)]['GPA'])
    st.write('Current diet: ' + df.iloc[int(prompt)]['diet_current'])
except Exception:
    st.write('Student with specified index does not exist')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
def regen():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
st.button('Regenerate', on_click=regen, key=None)

