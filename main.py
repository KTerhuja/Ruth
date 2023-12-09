import json
import time
import random 


import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

st.header('24/7 Rizz service for Miss Bunny 🐇', divider='rainbow')

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_file = load_lottiefile('animations/love.json')

with open ('pickup.txt', 'r') as f:

    text = f.readlines()


# lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"

st_lottie(lottie_file, key="user", height=300, speed=0.01)


def get_rizz(text): 

    rizz = random.choices(text)
    rizz = rizz[0].strip('\n')

    return rizz


if st.button('KhRizz'):
    rizz = get_rizz(text)
    st.write(rizz)
