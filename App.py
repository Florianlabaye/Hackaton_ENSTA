# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

#General settings
st.set_page_config(
    page_title="Energy optimization",
    page_icon="👋",
    layout="wide",
)

st.markdown("<h1 style='text-align: center; color: black;text-shadow: 2px 4px 3px rgba(0,0,0,0.3);margin-top: 0px;'>Artificial intelligence for energy optimization</h1>", unsafe_allow_html=True)

st.text("")
st.text("")

video_file = open('video.mp4', 'rb')

video_bytes = video_file.read()
st.video(video_bytes)

st.markdown("<h1 style='color: black;text-decoration:underline solid #000000;font-size:25px'>Estimate the energy consumption of your housing</h1>", unsafe_allow_html=True)

#st.subheader("A voir")

st.sidebar.markdown("# Welcome 🎈")



use_example = "Arg 1"
use_upload = "Arg 2"
use_text_input = "Arg 3"
use_url = "Arg 4"

input_method = st.radio(
    label="Select",
    options=[use_example, use_upload, use_text_input, use_url],
)

st.subheader(input_method)
