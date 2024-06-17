import json
import os
import pdb
import subprocess
import sys
import click

from pathlib import Path

# represent the root pachage that is doc
root = Path("doc")

# iterated package module with full path
module_list = []


def iterate_folder(path: Path):
    """iterate the given folder in current work space and form the /doc folder structure

    Args:
        path (Path): the given path to project directory
    """
    for entry in path.iterdir():
        if entry.is_dir():
            # iterate inside if the entry is folder
            iterate_folder(entry)

        elif entry.suffix == ".py":
            # changing root to /doc
            new_path = root / entry
            temp = list(new_path.parts)
            temp.pop(1)

            # creating relative md file
            new_path = Path(*temp).with_suffix(".md")
            new_path.parent.mkdir(parents=True, exist_ok=True)
            new_path.touch(exist_ok=True)
            module_list.append(new_path)


def create_doc_struct_file():
    """creating mkdocstructure.json"""
    doc_struct = []
    for module in module_list:
        doc_struct.append(dict(title="", descreption="", path=str(module)))

    with open("mkdocstructure.json", mode="w") as file:
        json.dump(doc_struct, file, indent=4)

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
def form_mkdocs():
    pass

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
    subprocess.call("mkdocs new .")
    iterate_folder(path)
    create_doc_struct_file()


if __name__ == "__main__":
    main()
