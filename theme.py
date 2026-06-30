import streamlit as st
from icons import icon, GITHUB_SVG, LINKEDIN_SVG, MAIL_SVG


def get_theme():
    """Returns (is_dark, colors_dict). Call once per page, before anything else renders."""
    theme_base = st.get_option("theme.base")
    is_dark = theme_base == "dark"

    if is_dark:
        colors = {
            "bg": "#0e1117",
            "card_bg": "#161b22",
            "border": "#2a2f3a",
            "text_primary": "#f5f5f5",
            "text_secondary": "#aaaaaa",
            "text_muted": "#777777",
            "hover_shadow": "rgba(0,0,0,0.45)",
            "sidebar_bg": "#10141c",
            "icon_color": "#f5f5f5",
        }
    else:
        colors = {
            "bg": "#ffffff",
            "card_bg": "#ffffff",
            "border": "#e5e5e5",
            "text_primary": "#111111",
            "text_secondary": "#555555",
            "text_muted": "#888888",
            "hover_shadow": "rgba(0,0,0,0.08)",
            "sidebar_bg": "#fafafa",
            "icon_color": "#1a1a1a",
        }
    return is_dark, colors, theme_base


def inject_base_css(colors):
    c = colors
    st.markdown(
        f"""
        <style>
            .stApp {{ background-color: {c['bg']}; }}

            /* Top header bar + toolbar - match the app background instead of Streamlit's default */
            [data-testid="stHeader"] {{
                background-color: {c['bg']};
            }}
            [data-testid="stToolbar"] {{
                background-color: {c['bg']};
            }}
            [data-testid="stDecoration"] {{ display: none; }}
            [data-testid="stSidebarNav"] {{ display: none; }}

            h1, h2, h3 {{ color: {c['text_primary']}; font-weight: 700; }}
            p, span, label, .stMarkdown {{ color: {c['text_primary']}; }}

            .project-card {{
                border: 1px solid {c['border']};
                border-radius: 14px;
                padding: 20px 22px;
                margin-bottom: 18px;
                background: {c['card_bg']};
                transition: box-shadow 0.15s ease, transform 0.15s ease;
            }}
            .project-card:hover {{
                box-shadow: 0 6px 18px {c['hover_shadow']};
                transform: translateY(-2px);
            }}
            .project-card p {{ color: {c['text_secondary']}; }}
            .project-card .demo-tag {{ color: {c['text_muted']}; }}

            .chip {{
                display: inline-block;
                padding: 3px 10px;
                border-radius: 999px;
                font-size: 12.5px;
                font-weight: 600;
                margin-right: 6px;
                margin-top: 6px;
                color: #ffffff;
            }}

            .icon-row {{ display: flex; align-items: center; gap: 14px; }}
            .icon-link {{ text-decoration: none; display: flex; align-items: center; }}
            .icon-link svg {{ transition: opacity 0.15s ease; }}
            .icon-link:hover svg {{ opacity: 0.65; }}

            .accent-bar {{
                height: 4px;
                border-radius: 4px;
                margin-bottom: 10px;
            }}

            /* ---------- Sidebar ---------- */
            section[data-testid="stSidebar"] {{
                background-color: {c['sidebar_bg']};
                border-right: 1px solid {c['border']};
            }}
            section[data-testid="stSidebar"] * {{
                color: {c['text_primary']} !important;
                font-size: 17px !important;
            }}
            section[data-testid="stSidebar"] h1,
            section[data-testid="stSidebar"] h2 {{
                font-size: 21px !important;
                font-weight: 700 !important;
            }}
            section[data-testid="stSidebar"] a {{
                font-size: 17px !important;
                font-weight: 500;
                padding: 8px 4px;
            }}
            section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {{
                border-radius: 8px;
                margin-bottom: 2px;
            }}
            section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"]:hover {{
                background-color: {c['border']};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(colors, theme_base):
    c = colors
    with st.sidebar:
        st.markdown("## Dhruv Gupta")
        st.markdown("AI Automations Engineer in progress")
        st.divider()
        st.page_link("streamlit_app.py", label="Home")
        from projects_config import PROJECTS
        for project in PROJECTS:
            st.page_link(f"pages/{project['page_file']}", label=project["name"])
        st.divider()
        st.markdown(
            f"""
            <div class="icon-row">
                <a class="icon-link" href="https://github.com/BeastBoom" target="_blank">{icon(GITHUB_SVG, 24, c['icon_color'])}</a>
                <a class="icon-link" href="https://linkedin.com/in/dhruv-gupta2006" target="_blank">{icon(LINKEDIN_SVG, 24, "#0a66c2")}</a>
                <a class="icon-link" href="mailto:dhruvgupt023@gmail.com">{icon(MAIL_SVG, 24, c['icon_color'])}</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.divider()
        st.caption(f"Theme: {theme_base or 'light'}")


def setup_page():
    """Call this first thing on every page (home and every page in pages/). Returns colors dict."""
    is_dark, colors, theme_base = get_theme()
    inject_base_css(colors)
    render_sidebar(colors, theme_base)
    return colors