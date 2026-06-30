import streamlit as st
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from icons import icon, GITHUB_SVG
from runner import run_script_with_file_io
from theme import setup_page

st.set_page_config(page_title="Text Analyzer — Dhruv Gupta", page_icon="🟢", layout="centered")

colors = setup_page()
icon_color = colors["icon_color"]

GITHUB_FOLDER_URL = "https://github.com/BeastBoom/Road-To-Creation/tree/main/Projects/Text%20Analyzer"
PROJECT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "Projects", "Text Analyzer",
)

st.markdown(
    f"""
    <div class="accent-bar" style="background:#65a30d; width:120px;"></div>
    <h1>Text Analyzer CLI</h1>
    <p style="font-size:14.5px;">Upload a .txt file. The original script runs unmodified and returns the top 10 most frequent words, stopwords excluded.</p>
    <a class="icon-link" href="{GITHUB_FOLDER_URL}" target="_blank">{icon(GITHUB_SVG, 18, icon_color)} &nbsp;View source on GitHub</a>
    """,
    unsafe_allow_html=True,
)

st.divider()

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    if st.button("Run analysis", type="primary"):
        with st.spinner("Running text_analyzer.py..."):
            success, stdout, stderr, output_bytes = run_script_with_file_io(
                project_folder=PROJECT_DIR,
                script_filename="text_analyzer.py",
                uploaded_file_bytes=uploaded_file.getvalue(),
                input_filename="file.txt",
                output_filename="word_counts.json",
            )

        if success:
            st.success("Done.")
            data = json.loads(output_bytes)

            st.markdown("### Top 10 words")
            st.table(
                [{"word": w, "count": c} for w, c in data]
            )

            st.download_button(
                "Download word_counts.json",
                data=output_bytes,
                file_name="word_counts.json",
                mime="application/json",
            )

            with st.expander("Raw script output"):
                st.code(stdout or "(no stdout)")
        else:
            st.error("The script did not run successfully.")
            with st.expander("Error details"):
                st.code(stderr or "Unknown error")
else:
    st.caption("No file uploaded yet.")