# Welcome to Auto MkDocs library

## installing dependency

```
pip install git+https://github.com/mohammadrezarouhani/auto_mkdocs.git
```


## notes
<ol>
  <li> if you want to add a functions or classes to your document, it must have docstring,  its very important</li>
  <li> there will be some warning after building project some of them are related to your project </li>
  <li> if you get some error when serving your project, your code has problems, check imports and relation base by the error code</li>
  <li> you should comply all statndard of python language inorder to get a good result</li>
</ol>

## Initialyze document structure

run command for initialyze: <br/>
```bash 
auto_mkdocs init << your project path >>
```

the command above will form docs folder base by your projects structure and 
create a mkdocs.yaml file with default theme and configurations 


## Serve the project in development server

``` bash
auto_mkdocs serve
```

## Build the document file

for build the documents in current folder run:
```bash
auto_mkdocs build 
```


there will be some warning about nav tags structure that should be a list not dict, this doesnt make any problem 
<h1 style="text-align:center; border-bottom:1px solid red; "> THE END</h1>

```
                                    ⣿⣿⣿⣿⣿⣿⠏⠌⣾⣿⣿
                                    ⣿⣿⣿⣿⣿⠀⠀⠸⠿⣿⣿⣿
                                    ⣿⣿⣿⣿⠃⠀⣠⣾⣿⣿⣿
                                    ⣿⣿⡿⠃⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                    ⣿⣿⠃⠀⠀⣾⣿⣿⣿⣿⣿⣦⠀⠈⠻⣿⣿⣿
                                    ⣿⣿⠀⠀⠀⣿⣿⣿⠟⠉⠉⠉⢃⣤⠀⠈⢿⣿⣿⣿
                                    ⣿⣿⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⢹⣿⣧⠀⠀⠙⣿⣿
                                    ⣿⣿⡆⠀⠀⠈⠻⡅⠀⠀⠀⠀⣸⣿⠿⠇⠀⠀⢸⣿
                                    ⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠔⠛⠁⠀⠀⠀⣠⣿⣿
                                    ⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿
                                    ⣿⣿⣿⠃    Guts    ⣠⣾⣿⣿
                                    ⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿
                                    ⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿
                                    ⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
                                    ⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿
                                    ⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿
                                    ⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿
                                    ⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
```
