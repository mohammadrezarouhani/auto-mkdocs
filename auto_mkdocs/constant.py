from typing import List
from pathlib import Path, WindowsPath

PACKAGE_PATH = ""

MD_PATH_LIST: List[WindowsPath] = []

DOCUMENT_ROOT = Path("docs")
NAV = []
GRAY_LIST = [
    ".venv",
    "__pycache__",
    "__init__",
    "setup",
    ".env",
    ".venv",
    "env",
    "venv",
    "ENV",
    "env.bak",
    "venv.bak",
]

CONFIG = {
    "site_name": "",
    "site_description": "",
    "repo_url": "",
    "site_url": "",
    "site_author": "",
    "repo_name": "",
    "copyright": "",
    "theme": {
        "name": "material",
        "palette": [
            {
                "media": "(prefers-color-scheme: light)",
                "scheme": "default",
                "primary": "blue grey",
                "accent": "indigo",
                "toggle": {
                    "icon": "material/lightbulb-outline",
                    "name": "Switch to dark mode",
                },
            },
            {
                "media": "(prefers-color-scheme: dark)",
                "scheme": "slate",
                "primary": "blue grey",
                "accent": "indigo",
                "toggle": {
                    "icon": "material/lightbulb",
                    "name": "Switch to light mode",
                },
            },
        ],
        "features": [
            "content.code.annotate",
            "content.tabs.link",
            "content.code.copy",
            "announce.dismiss",
            "navigation.tabs",
            "search.suggest",
            "search.highlight",
        ],
    },
    "plugins": ["mkdocstrings", "search"],
}
