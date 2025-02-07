

import numpy as np

import pandas as pd
import streamlit as st

st.title("HELLO EVERYONE , WE ARE LEARNING PYTHON")
st.write("PYTHON REQUIRES PRACTICE")

data = pd.DataFrame({
    'c1':[10,20,30,40],
    'c2':['A','B','C','D']})

st.write("BELOW IS THE TABLE FOR DATA")
st.write(data)

chart_data=pd.DataFrame(np.random.rand(20,3),
                        columns=['A','B','C'])

st.bar_chart(chart_data)

