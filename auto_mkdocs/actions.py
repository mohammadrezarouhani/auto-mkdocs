import os
import yaml

from pathlib import Path

from .constant import *


def generate_md_files(module_path: WindowsPath) -> WindowsPath:
    """get the target module path and create a md file in doc folder

    Args:
        module_path (WindowsPath): target module path in our project

    Returns:
        (WindowsPath): the path to the md file
    """
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
    package_content = path.iterdir()

    for entry in package_content:
        if entry.stem in GRAY_LIST:
            continue

        # check path not in gray list
        elif entry.suffix == ".py":
            res = generate_md_files(entry)
            generated_target_path.append(res)

        # iterate over if the path is folder
        elif entry.is_dir():
            generated_target_path = iterate_package(entry, generated_target_path)

    return generated_target_path


def mov_README_file(path: Path):
    """move the README file of taget package to index.md

    Args:
        path (Path): target pckage path
    """
    file_path = os.path.join(path, "README.md")

    index_path = Path("docs/index.md")
    if not index_path.exists():
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.touch(exist_ok=True)

    if os.path.exists(file_path):
        with open(file_path) as file:
            content = file.read()

        with open("docs/index.md", mode="w") as file:
            file.write(content)
    else:
        with open("docs/index.md", mode="w") as file:
            file.write("#welcome to project documentation")

    return Path("docs/README.md")


def create_mkdocs_conf(navigations, site_name="", site_description="", site_author=""):
    """create a default configuration for mkdoc

    Args:
        site_name (str, optional): project name. Defaults to "".
        site_description (str, optional): project description. Defaults to "".
        site_author (str, optional): project owner . Defaults to "".
    """
    CONFIG["site_name"] = site_name
    CONFIG["site_description"] = site_description
    CONFIG["site_author"] = site_author
    CONFIG["nav"] = navigations

    with open("mkdocs.yml", mode="w") as file:
        yaml.dump(CONFIG, file, sort_keys=False, indent=4)


def convert_path_to_dict(path: WindowsPath, path_dict={}) -> dict:
    """convert path window to nested dict object

    Args:
        path (WindowsPath): target window path
        path_dict (dict, optional): final result , updating step by step. Defaults to {}.

    Returns:
        dict: window path converted to nested dict
    """
    if not path.parent.name:
        return path_dict
    elif path.suffix:
        target_path = Path(*path.parts[1:])
        return convert_path_to_dict(
            path.parent, {path.stem: str(target_path).replace("\\", "/")}
        )
    else:
        path_dict = {path.name: path_dict}
        return convert_path_to_dict(path.parent, path_dict)


def create_nav_collection(pathes: List[WindowsPath]) -> List[dict]:
    """return pathes of moudles as a list of nested dict

    Args:
        pathes (List[WindowsPath]): list of target window path

    Returns:
        List[dict]: list of nested dict repr windown pathes
    """
    return [convert_path_to_dict(path) for path in pathes]


def proccess_map(map, dist_map) -> dict:
    """processing map, merge modules with the same folder

    Args:
        map (dict): the passed map should be merged
        dist_map (dict): target map should be passed

    Returns:
        dict: merged dict
    """
    key = next(iter(map))
    value = map.get(key)

    dist_key = next(iter(dist_map))
    dist_value = dist_map[dist_key]

    if type(value) == dict and type(dist_value) == dict and key == dist_key:
        res = proccess_map(value, dist_value)
        dist_map[key] = res
    else:
        dist_map.update(map)
        return dist_map

    return dist_map


def merge_navigations_dicts(mappers: List[dict]) -> List[dict]:
    """form the mkdocs.yaml nav tag

    Args:
        mappers (List[dict]): list of target project module path as nested dict

    Returns:
        List[dict]: merged module with the same parent directory
    """
    results = []
    for m in mappers:
        key = next(iter(m))

        for res in results:
            res_key = next(iter(res))

            if res_key == key:
                dist_map = proccess_map(m, res)
                results.remove(res)
                results.append(dist_map)
                break
        else:
            results.append(m)
    return results


def proccess_path(path: Path):
    parts = path.parts
    if len(parts) > 1:
        os.chdir(path.parent)
        return Path(parts[-1])
    else:
        return path


def convert_nav_to_list(key, value):

    if type(value) == dict:
        return {
            key: [
                (
                    {nav_key: nav_value}
                    if type(nav_value) == str
                    else convert_nav_to_list(nav_key, nav_value)
                )
                for nav_key, nav_value in value.items()
            ]
        }
    else:
        return {key: value}


def make_nav(merged_nav) -> list:
    result = []
    for nav in merged_nav:
        key = next(iter(nav))
        value = nav[key]
        new = convert_nav_to_list(key, value)
        result.append(new)

    result.insert(0, {"Welcome To Mkdoc Document": "index.md"})
    return result
