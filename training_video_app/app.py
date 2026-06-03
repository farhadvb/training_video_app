import streamlit as st
from pathlib import Path
import json

st.set_page_config(
    "نمایش فایلهای آموزشی شرکت JPC",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=["a","b","c"]
)

# -----------------------------
# Load CSS
# -----------------------------
def load_css(css_file:str):
    pass