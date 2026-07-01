"""
Add a new project by adding one dict to PROJECTS below.
Nothing else needs to change when you add a project.

Fields:
  name            : Display name
  page_file       : Exact filename of this project's page inside pages/ (e.g. "1_Text_Analyzer.py")
  description     : One or two lines, shown on the home page card
  tech            : list of tech tags shown as colored chips
  github_url      : link to the project's folder on GitHub (not the repo root)
  accent          : one of "lime", "red", "orange", "sky", "teal" - controls the card's accent color
  live_demo       : True if the page actually runs the project, False if it's GitHub + screenshots only
  cover_emoji_svg : a short inline identifier (kept minimal, used only as a fallback bullet, not decoration)
"""

PROJECTS = [
    {
        "name": "Text Analyzer CLI",
        "page_file": "1_Text_Analyzer.py",
        "description": "Reads a .txt file, strips stopwords, and surfaces the top 10 most frequent words as JSON.",
        "tech": ["Python", "JSON", "CLI"],
        "github_url": "https://github.com/BeastBoom/Road-To-Creation/tree/main/Projects/Text%20Analyzer",
        "accent": "lime",
        "live_demo": True,

    },
    {
        "name": "ML Classifier Comparison",
        "page_file": "2_ML_Classifier_Comparison.py",
        "description": "Trained and compared Logistic Regression, Decision Tree, and Random Forest classifiers on the Titanic survival dataset, evaluated on accuracy and F1 score.",
        "tech": ["Python", "Pandas", "scikit-learn"],
        "github_url": "https://github.com/BeastBoom/Road-To-Creation/tree/main/Projects/Logistic-Decision-Random-Machine%20Learning",
        "accent": "orange",
        "live_demo": True,
    },
    {
        "name": "Bank App",
        "page_file": "3_Bank_App.py",
        "description": "Simulated multi-account banking system with deposits, withdrawals, transfers, daily limits, and rollback-safe transaction logging.",
        "tech": ["Python", "Pandas", "OOP"],
        "github_url": "https://github.com/BeastBoom/Road-To-Creation/tree/main/Projects/Bank%20App",
        "accent": "orange",
        "live_demo": True,
    }
]

ACCENT_COLORS = {
    "lime":   "#65a30d",
    "red":    "#dc2626",
    "orange": "#ea580c",
    "sky":    "#0284c7",
    "teal":   "#0d9488",
}
