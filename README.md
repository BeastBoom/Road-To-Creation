# Dhruv Gupta — Project Portfolio

**Live site: [road-to-creation.streamlit.app](https://road-to-creation.streamlit.app/)**

A Streamlit-based portfolio. The home page lists every project as a card; each card links to a dedicated page that either runs the project live in-browser or shows the GitHub source plus screenshots/video.

## Structure
```
streamlit_app.py          Home page (project cards, auto-built from projects_config.py)
projects_config.py        Add one entry here per project — nothing else needs to change
icons.py                  Shared SVG icons + theme CSS
runner.py                 Runs a project's original script unmodified via subprocess
pages/
    1_Text_Analyzer.py     One page per live-demo project
Projects/
    Text Analyzer/
        text_analyzer.py    Original script, never modified
        README.md
```

## Adding a new project
1. Drop the project folder into `Projects/`.
2. If it can run as a live demo: copy `pages/1_Text_Analyzer.py`, point it at the new folder/script/input/output filenames.
3. If it can't run live (needs a DB, server, etc.): skip step 2, just add screenshots/video to the project folder.
4. Add one entry to `PROJECTS` in `projects_config.py`. Done — it shows up on the home page automatically.

## Run locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deployment
Deployed on [Streamlit Community Cloud](https://streamlit.io/cloud), pointed at `streamlit_app.py` on `main`.
