import pdb
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
@click.option(
    "--path",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
    help="path to project",
    required=True,
)
@click.option("--name", help="path to project")
@click.option("--desc", help="project description")
@click.option("--author", help="project author")
@click.option("--ignore", help="ignoring file path")
def init(path, ignore, name, desc, author):
    click.echo("Welcome To auto_mkdocs", color=True)

    project_name = name
    project_description = desc
    author_name = author
    GRAY_LIST.extend(ignore.split(","))

    path = proccess_path(path)

    # moving the project README FIle to Welcome Page of document
    mov_README_file(path)

    # iterate over project and return the relative path of project
    docs_path = iterate_package(path)

    # create dict mapper to project modules, it convert the path to nested dict's
    nav_dict = create_nav_collection(docs_path)

    # create nav setting base by the created mapper
    merged_nav = merge_navigations_dicts(nav_dict)

    # convert merged path dict to list
    navigations_list = make_nav(merged_nav)

    # create a config file base by default setting and created mapper
    create_mkdocs_conf(navigations_list, project_name, project_description, author_name)
    click.echo("Config File and docs folder created!", color=True)


@main.command("serve", help="serve the document in development server")
def serve():
    subprocess.run(["python", "-W ignore::DeprecationWarning", "-m", "mkdocs", "serve"])


@main.command("build", help="build the document file in current folder")
def serve():
    subprocess.run(["python", "-W ignore::DeprecationWarning", "-m", "mkdocs", "build"])


if __name__ == "__main__":
    main()
