from setuptools import setup

setup(
    name="auto_mkdocs",
    version="1.1.3",
    description="auto genrating document for python projects",
    author="mohammadreza rouhani",
    author_email="rezarouhanitonekaboni@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mohammadrezarouhani/auto_mkdocs",
    install_requires=open("requirements.txt").readlines(),
    entry_points={
        "console_scripts": [
            "auto_mkdocs = main:main",
        ],
    },
)
