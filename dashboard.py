import time
import streamlit as st
import requests
from PIL import Image
import controller
from model import multi_tab

st.title("Card Fraud Detection Dashboard")
st.sidebar.title("Data Themes")

sidebar_options = st.sidebar.selectbox(
    "Options",
    ("EDA", "Training", "Inference")
)

if sidebar_options == "EDA":
    controller.EDA()

elif sidebar_options == "Training":
    controller.train()

else:
    controller.infer()
