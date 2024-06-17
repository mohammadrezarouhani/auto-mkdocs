from distutils.core import setup

setup(
    name="Auto MkDoc",
    version="1.0",
    description="auto genrating document for python packages",
    author="Guts",
    author_email="",
    url="",
    packages=["mkdocs", "mkdocs-material", "mkdocstrings-python"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "auto_mkdoc = generate_script:main",
        ],
    },
)
