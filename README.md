# Python-Project-Script-Setup (PPSS)
Project setup script that depends on pyenv. It asks you for a project name and then
- creates folder with that name
- makes a new pyenv-virtualenv with your project name
- sets up a .python-version file in project home
- uses pip to install black and pylint in the virtualenv
- creates a .pylintrc file for customization in project home

# requirements
- Python 3.10.3
- Pip 22.0.4
- [Pyenv](https://github.com/pyenv/pyenv)
- [Pyenv-Virtualenv](https://github.com/pyenv/pyenv-virtualenv)


# instructions
Unless specified this script will create a new python project in the directory you run this. You are able to pass a path variable with CLI if you so choose.
Make sure [pyenv](https://github.com/pyenv/pyenv) is installed you can find the githup at the link. If you are on mac and have homebrew you can run:
```
brew install pyenv
```
Configure your shell's environment for pyenv. The instructions are on the pyenv github page. 
This lets the .python-version change the pyenv version when you cd into the project.

# comandline options:


```
usage: ppss.py [-h] [-a] [-n NAME] [--path PATH]

options:
  -h, --help           show this help message and exit
  -a, -all             Runs full script, minimal interaction possible
                       depending on argumenst passed.
  -n NAME, -name NAME  Input your project name
  --path PATH          Path to the python project directory
```

# customization
You can change PROJECT_PATH to where all your python projects live.
You can add more Pip instructions by adding to this line:

```
os.system(
            "/Users/Emilienne/.pyenv/versions/"
            + project_name
            + "/bin/python -m pip install black pylint"
        )
        
```
Right now it is configure to install [black](https://github.com/psf/black) and [pylint](https://github.com/PyCQA/pylint).
