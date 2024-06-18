from multiprocessing import Value
import os
import pdb
import sys
from turtle import pd
import yaml
import click

from pathlib import Path, WindowsPath
from collections import OrderedDict
from constant import *


def generate_md_files(module_path: WindowsPath):

    # add docs folder as root
    nav_url = DOCUMENT_ROOT / module_path
    temp = list(nav_url.parts)
    temp.pop(1)

    # change the suffix to .md
    nav_url = Path(*temp).with_suffix(".md")

    # creating parent folder and target module md file
    nav_url.parent.mkdir(parents=True, exist_ok=True)
    nav_url.touch(exist_ok=True)

    # writing the module mapper in md files handles in linux and windows
    # change the file system path to md readble mapper
    if "/" in str(module_path):
        md_path = ":::" + str(module_path).replace("/", ".")
    else:
        md_path = ":::" + str(module_path).replace("\\", ".")

    # removing the suffix from md_path
    md_path = os.path.splitext(md_path)[0]

    # write the mapper to target md file
    with open(nav_url, mode="w") as file:
        file.write(md_path)

    return nav_url


def iterate_package(path: WindowsPath, generated_target_path=[]) -> List[WindowsPath]:
    """iterate the given folder in current work space and form the /doc folder structure

    Args:
        path (Path): the given path to project directory
        generated_target_path (List(WindowPath)): python file inside target package

    Returns:
        (List[WindowsPath]): all of the gathered python files
    """
    package_content=path.iterdir()
    
    for entry in package_content:
        if entry.stem in GRAY_LIST:
            continue

        elif entry.suffix == ".py":
            # check path not in gray list
            res = generate_md_files(entry)
            generated_target_path.append(res)

        elif entry.is_dir():
            # iterate over if the path is folder
            generated_target_path = iterate_package(entry, generated_target_path)

    return generated_target_path


def mov_README_file(path: Path):
    """mov the README file of taget package to index.md

    Args:
        path (Path): target pckage path
    """
    file_path = os.path.join(path, "README.md")

    if os.path.exists(file_path):
        with open(file_path) as file:
            content = file.read()

        with open("docs/index.md", mode="w") as file:
            file.write(content)


def create_mkdocs_conf(site_name="", site_description="", site_author=""):
    CONFIG["site_name"] = site_name
    CONFIG["site_description"] = site_description
    CONFIG["site_author"] = site_author

    with open("mkdocs.yml", mode="w") as file:
        yaml.dump(CONFIG, file, sort_keys=False, indent=4)


def create_nav_bar():
    """creating structure.json"""
    navigation = []
    for path in MD_PATH_LIST:
        mapper = {}

        while str(path) != "docs":
            if mapper:
                mapper = {str(path.stem): mapper}
            else:
                mapper = {str(path.stem): path.name}

            path = path.parent

        else:
            navigation.append(mapper)

    pdb.set_trace()


@click.command("main")
@click.version_option("1.0.0", prog_name="Auto MkDoc Generator")
@click.argument(
    "path",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
)
def main(path):
    # click.echo("Welcome To AutoMkDocs", color=True)
    # click.prompt("please enter the site name:")
    # click.prompt("please enter the site_description name:")
    # click.prompt("please enter the author name:")

    # iterate over the target package and gathering all python files
    res = iterate_package(path)
    MD_PATH_LIST.extend(res)
    mov_README_file(path)
    create_mkdocs_conf()
    # create_nav_bar()


if __name__ == "__main__":
    main()
