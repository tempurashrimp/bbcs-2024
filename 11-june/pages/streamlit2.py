import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='kaveh', page_icon='🏛️')

st.markdown("# Page 2 ")
st.sidebar.markdown("# Page 2 ")

with st.container():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    from sklearn.datasets import load_digits
    df = pd.DataFrame(np.random.randn(50, 2) / [100, 100] + [1.2963,103.8502], columns=['lat', 'lon'])

    st.map(df)

    digits = load_digits()
    hist = plt.hist(digits['target'], edgecolor='black')
    st.pyplot()