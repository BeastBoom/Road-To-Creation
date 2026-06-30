import streamlit as st
from projects_config import PROJECTS, ACCENT_COLORS
from icons import icon, GITHUB_SVG, LINKEDIN_SVG, MAIL_SVG
from theme import setup_page

st.set_page_config(
    page_title="Dhruv Gupta — Portfolio",
    page_icon="🟢",
    layout="wide",
)

colors = setup_page()
icon_color = colors["icon_color"]

# ---------- Header ----------
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("# Dhruv Gupta")
    st.markdown(
        "AI Automations Engineer in progress — Python, data, automation, and shipped projects."
    )
with col2:
    st.markdown(
        f"""
        <div class="icon-row" style="justify-content:flex-end; margin-top:18px;">
            <a class="icon-link" href="https://github.com/BeastBoom" target="_blank">{icon(GITHUB_SVG, 26, icon_color)}</a>
            <a class="icon-link" href="https://linkedin.com/in/dhruv-gupta2006" target="_blank">{icon(LINKEDIN_SVG, 26, "#0a66c2")}</a>
            <a class="icon-link" href="mailto:dhruvgupt023@gmail.com">{icon(MAIL_SVG, 26, icon_color)}</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()
st.markdown("## Projects")

if not PROJECTS:
    st.info("No projects added yet. Add one in projects_config.py.")

# ---------- Project cards ----------
cols = st.columns(2)
for i, project in enumerate(PROJECTS):
    accent_hex = ACCENT_COLORS.get(project["accent"], "#0d9488")
    chips_html = "".join(
        f'<span class="chip" style="background:{accent_hex};">{t}</span>'
        for t in project["tech"]
    )
    demo_tag = "Live demo" if project["live_demo"] else "Code + docs only"

    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="project-card">
                <div class="accent-bar" style="background:{accent_hex};"></div>
                <h3 style="margin-bottom:2px;">{project['name']}</h3>
                <p style="font-size:14.5px; margin-top:4px;">{project['description']}</p>
                <div>{chips_html}</div>
                <p class="demo-tag" style="font-size:12.5px; margin-top:10px;">{demo_tag}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        b1, b2 = st.columns(2)
        with b1:
            st.page_link(f"pages/{project['page_file']}", label="Open project", icon=None)
        with b2:
            st.markdown(
                f'<a class="icon-link" href="{project["github_url"]}" target="_blank">'
                f'{icon(GITHUB_SVG, 20, icon_color)} &nbsp;GitHub folder</a>',
                unsafe_allow_html=True,
            )