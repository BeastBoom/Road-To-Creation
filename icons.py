"""
Real SVG logo markup - never emoji. Add new icons here as you need them.
Source: official simple-icons paths (single color, recolored via fill).
"""

GITHUB_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}">
<path d="M12 .5C5.73.5.5 5.73.5 12c0 5.08 3.29 9.39 7.86 10.91.57.1.78-.25.78-.55
0-.27-.01-1.16-.02-2.1-3.2.7-3.88-1.36-3.88-1.36-.52-1.33-1.28-1.69-1.28-1.69
-1.04-.71.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.76 2.7 1.25 3.36.96
.1-.75.4-1.25.73-1.54-2.56-.29-5.25-1.28-5.25-5.7 0-1.26.45-2.29 1.19-3.1
-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11.05 11.05 0 0 1 5.79 0
c2.21-1.49 3.18-1.18 3.18-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.84 1.19 3.1
0 4.43-2.69 5.41-5.26 5.69.41.36.78 1.07.78 2.15 0 1.55-.01 2.8-.01 3.18
0 .3.21.66.79.55A10.52 10.52 0 0 0 23.5 12C23.5 5.73 18.27.5 12 .5z"/>
</svg>"""

LINKEDIN_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}">
<path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05
c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/>
</svg>"""

MAIL_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2">
<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>
</svg>"""

EXTERNAL_LINK_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2">
<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6"/><path d="M10 14 21 3"/>
</svg>"""


def icon(svg_template: str, size: int = 20, color: str = "#1a1a1a") -> str:
    return svg_template.format(size=size, color=color)


BASE_CSS = """
<style>
    .stApp { background-color: #ffffff; }

    h1, h2, h3 { color: #111111; font-weight: 700; }

    .project-card {
        border: 1px solid #e5e5e5;
        border-radius: 14px;
        padding: 20px 22px;
        margin-bottom: 18px;
        background: #ffffff;
        transition: box-shadow 0.15s ease, transform 0.15s ease;
    }
    .project-card:hover {
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }

    .chip {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 12.5px;
        font-weight: 600;
        margin-right: 6px;
        margin-top: 6px;
        color: #ffffff;
    }

    .icon-row { display: flex; align-items: center; gap: 10px; }
    .icon-link { text-decoration: none; }

    .accent-bar {
        height: 4px;
        border-radius: 4px;
        margin-bottom: 10px;
    }
</style>
"""
