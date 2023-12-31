import json
import time
import random 


import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


st.header('24/7 Rizz Service for My Bunny 🐇', divider='rainbow')

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


if st.button('Tab here to get KhRizz!'):
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
text-align: center; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Developed by <a style='display: inline; text-align: center;' href="https://www.virtusa.com/" target="_blank">Virtusa <img src = "data:image/jpeg;base64,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" height = "15"> </a><br 'style= top:3px;'> 
Data & Analytics Team  </a><br 'style= top:3px;'>
Dataset Source: https://www.niddk.nih.gov <a style='display: inline; text-align: center;' href="https://www.niddk.nih.gov/about-niddk/strategic-plans-reports/usrds/data-query-tools/esrd-incident-count" target="_blank"></a><br 'style= top:3px;'> 
</a></p>
</div>

</div>
"""



