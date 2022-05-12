# Python-Project-Setup-Script (PPSS)
Project setup script that depends on pyenv. It:
- creates a new project directory (name specified by you)
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

# creating symlink

You can create a symlink that will let you execute this script from anywhere making it much more useful.
1. git clone repository
```
git clone https://github.com/EmZaid/Python-Project-Setup-Script
```
2. make the ppss file executable. 
```
chmod +x ppss
```
Note: It is the same script just with the .py taken off. You can verify this by running:
```
diff ppss.py ppss
```
3. make the symlink:
```
ln -s <location_of_ppss> /usr/local/bin/ppss
```
4. You can now run this script by typing `ppss` and passing arguments.
```
ppss -an project_name --path ~/Documents
```

# comandline options:


```
usage: ppss.py [-h] [-a] [-n NAME] [--path PATH]

options:
  -h, --help           show this help message and exit
  -a, -all             Runs full script, minimal interaction possible
                       depending on argumenst passed.
  -n NAME, -name NAME  Input your project name
  --path PATH          Path to the python project directory. If no path is supplied uses current working directory.
```

# customization

You can add more Pip instructions by adding to this line (line 163 in the python script):

```
160   os.system(
161            "~/.pyenv/versions/"
162           + project_name
163            + "/bin/python -m pip install black pylint"
        )
        
```
Right now it is configured to install [black](https://github.com/psf/black) and [pylint](https://github.com/PyCQA/pylint).
