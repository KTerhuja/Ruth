import json
import time
import random 


import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_file = load_lottiefile('animations/love.json')

with open ('pickup.txt', 'r') as f:

    text = f.readlines()


# lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"

st_lottie(lottie_file, key="user")


def get_rizz(): 

    rizz = random.choices(text)
    rizz = rizz[0].strip('\n')

    return rizz


st.button("Reset", type="primary")
if st.button('Say hello'):
    rizz = get_rizz()
    st.write(rizz)
