# Python-Pyenv-Project-Script
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
This script is set up to add a new project in your home directory `~/` you are free change this (just edit the PROJECT_PATH variable) as you see fit. 
Make sure [pyenv](https://github.com/pyenv/pyenv) is installed you can find the githup at the link. If you are on mac and have homebrew you can run:
```
brew install pyenv
```
Configure your shell's environment for pyenv. The instructions are on the pyenv github page. 
This lets the .python-version change the pyenv version when you cd into the project.


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
