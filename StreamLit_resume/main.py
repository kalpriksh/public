import streamlit as st
from PIL import Image

# creating a resume using streamLit

with st.sidebar:
    image = Image.open('image.jpg')
    st.image(image)


'''
## Hey there! I am Kalpriksh  \nData Scientist | Data Analyst  \n Adaptive, Technology enthusiast, neophile en route generalist
'''


'''
-----
## About Me
'''


exp_col, skill_col = st.columns(spec=[0.6,0.4])

with exp_col:
    '''
    ---
    ## Experience
    
    '''


with skill_col:
    '''
    ---
    ## Skills
    '''
    
    col1,col2 = st.columns(2)
    with col1:
        '''     
        - machine learning
        - deep learning
        - sql
        - python
        - nodejs
        - C# dotNet
        '''
    with col2:
        '''
        - data visualization
        - data analysis
        - data cleaning
        - data wrangling
        - data modeling
        '''

'''
---
## Education


'''





