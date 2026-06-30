import streamlit as st
import streamlit.components.v1 as components
import os

from icons import icon, GITHUB_SVG
from theme import setup_page

st.set_page_config(page_title="ML Classifier Comparison — Dhruv Gupta", page_icon="🟢", layout="centered")

colors = setup_page()
icon_color = colors["icon_color"]

GITHUB_FOLDER_URL = "https://github.com/BeastBoom/Road-To-Creation/tree/main/Projects/Logistic-Decision-Random-Machine%20Learning"
PROJECT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "Projects", "Logistic-Decision-Random-Machine Learning",
)
NOTEBOOK_HTML_PATH = os.path.join(PROJECT_DIR, "code.html")

st.markdown(
    f"""
    <div class="accent-bar" style="background:#f97316; width:120px;"></div>
    <h1>ML Classifier Comparison</h1>
    <p style="font-size:14.5px;">Logistic Regression, Decision Tree, and Random Forest trained on the Titanic dataset, compared on accuracy and F1 score. This is a static export of an already-executed notebook, not a live re-run.</p>
    <a class="icon-link" href="{GITHUB_FOLDER_URL}" target="_blank">{icon(GITHUB_SVG, 18, icon_color)} &nbsp;View source on GitHub</a>
    """,
    unsafe_allow_html=True,
)

st.divider()

if os.path.exists(NOTEBOOK_HTML_PATH):
    with open(NOTEBOOK_HTML_PATH, "r", encoding="utf-8") as f:
        notebook_html = f.read()
    components.html(notebook_html, height=2000, scrolling=True)
else:
    st.error("Notebook export not found. Make sure code.html is in the project folder.")
