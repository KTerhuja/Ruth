import json
import time

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_file = load_lottiefile('cat-lottie-file.json')


# lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"

st_lottie(lottie_file, key="user")
