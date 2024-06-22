import click
import subprocess

from pathlib import Path

from .constant import *
from .actions import *


@click.group(
    help="Auto MkDoc Generator - A tool to automate the creation of MkDocs projects."
)
@click.version_option("1.0.0", prog_name="Auto MkDoc Generator")
@click.pass_context
def main(ctx):
    ctx.ensure_object(dict)


@main.command(
    "init", help="Initialize a new MkDocs project in the specified directory."
)
@click.argument(
    "path",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
)
def init(path):
    click.echo(SIGNATURE)
    click.echo("Welcome To auto_mkdocs", color=True)
    project_name = click.prompt("please enter the project name")
    project_description = click.prompt("please enter the  project description")
    author_name = click.prompt("please enter the author name")

    # moving the project README FIle to Welcome Page of document
    mov_README_file(path)

    # iterate over project and return the relative path of project
    docs_path = iterate_package(path)

    # create dict mapper to project modules, it convert the path to nested dict's
    mappers = create_nav_collection(docs_path)

    # create nav setting base by the created mapper
    navigations = create_nav_bar(mappers)

    # create a config file base by default setting and created mapper
    create_mkdocs_conf(navigations, project_name, project_description, author_name)


@main.command("serve", help="serve the document in development server")
def serve():
    subprocess.run(["mkdocs", "serve"])


@main.command("build", help="build the document file in current folder")
def serve():
    subprocess.run(["mkdocs", "build"])


if __name__ == "__main__":
    main()
