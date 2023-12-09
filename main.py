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


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:0;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Developed with love<a style='display: inline; text-align: left;' target="_blank"> </a><br 'style= top:3px;'> 
Khries  </a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
