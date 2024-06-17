import os
import pdb
import yaml
import json
import click
from pathlib import Path

# represent the root pachage that is doc
root = Path("docs")

# iterated package module with full path
module_structure = {}


def iterate_folder(path: Path):
    """iterate the given folder in current work space and form the /doc folder structure

    Args:
        path (Path): the given path to project directory
    """
    for entry in path.iterdir():
        if entry.is_dir():
            # iterate inside if the entry is folder
            iterate_folder(entry)

        elif entry.suffix == ".py" and not '__init__' in str(entry):
            click.echo(entry)

            # changing root to /doc
            new_path = root / entry
            temp = list(new_path.parts)
            temp.pop(1)

            # creating relative md file
            new_path = Path(*temp).with_suffix(".md")
            new_path.parent.mkdir(parents=True, exist_ok=True)
            new_path.touch(exist_ok=True)

            if "//" in str(entry):
                md_path = str(entry).replace("//", ".")
            else:
                md_path = str(entry).replace("\\", ".")

            md_path=os.path.splitext(md_path)[0]

            with open(new_path, mode="w") as file:
                file.write(f":::{md_path}")


def create_doc_struct_file():
    """creating structure.json"""
    doc_struct = []
    for module in module_structure:
        doc_struct.append(dict(title="", descreption="", path=str(module)))

    with open("structure.json", mode="w") as file:
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
def main(path):
    iterate_folder(path)
    create_doc_struct_file()


if __name__ == "__main__":
    main()
