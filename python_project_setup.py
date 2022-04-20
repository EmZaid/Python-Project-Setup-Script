"""This is a script to set up a new python project"""
import os
import subprocess
import sys

# Change this to where you python projects live
PROJECT_PATH = "~/"

# The program will ask you what your project name will be
project_name = input("Project Name:")

new_proj_path = PROJECT_PATH + project_name + "/"


def create_folder():
    """This will create a new project in Python Projects"""

    try:
        os.mkdir(PROJECT_PATH + project_name)
    except OSError:
        print(f"(Creation of the directory {project_name} failed)")
    else:
        print(f"Successfully created the directory {project_name}")


def pyenv_options():
    """This gives the user options about creating a virutalenv"""

    accepted_answ = ["y", "n", "exit", "yes", "no"]
    yes_answ = ["y", "yes"]
    no_answ = ["n", "no"]

    answ = input("Do you want to create a new virtualenv? y/n/exit:")
    answ = answ.lower()

    while answ not in accepted_answ:
        answ = input("please enter: y/n/exit:")
        answ = answ.lower()
    while answ in yes_answ:
        # Creates a new virtualenv with your project name
        print("Ok. Creating virtualenv now:")
        subprocess.run(["pyenv", "virtualenv", project_name], check=True)
        return
    while answ in no_answ:
        print("Ok. Continuting on")
        return
    if answ == "exit":
        print("Exiting!")
        sys.exit(0)


def pyenv_local_options():
    """lets you create a .python-version file"""
    accepted_answ = ["y", "n", "exit", "yes", "no"]
    yes_answ = ["y", "yes"]
    no_answ = ["n", "no"]

    # This file, assuming you set up pyenv
    answ = input("Do you want to set up a .python-version file?")
    answ = answ.lower()

    while answ not in accepted_answ:
        answ = input("please enter: y/n/exit:")
        answ = answ.lower()
    while answ in yes_answ:
        print("Ok. Creating .python-version now:")
        os.system(
            "echo " + project_name + ">>" + new_proj_path + "/" + ".python-version"
        )
        return
    while answ in no_answ:
        print("Ok. Continuting on")
        return
    if answ == "exit":
        print("Exiting!")
        sys.exit()


def pip_install():
    """installs black and pylint and a .pylintrc file"""
    accepted_answ = ["y", "n", "exit", "yes", "no"]
    yes_answ = ["y", "yes"]
    no_answ = ["n", "no"]

    answ = input("Do you want install pylint and black:")
    answ = answ.lower()

    while answ not in accepted_answ:
        answ = input("please enter: y/n/exit:")
        answ = answ.lower()
    while answ in yes_answ:
        print("Ok. Creating .python-version now:")

        # Usually os.system is not used, but I couldn't find a way around this.
        # If I used subprocess.run() to activate the new venv it wouldn't register
        # and the pip install command would install on my 3.10.3 python version
        os.system(
            "/Users/Emilienne/.pyenv/versions/"
            + project_name
            + "/bin/python -m pip install black pylint"
        )

        os.chdir(new_proj_path)
        with open(".pylintrc", "w", encoding="UTF-8") as outfile:
            subprocess.run(["pylint", "--generate-rcfile"], check=True, stdout=outfile)

        return
    while answ in no_answ:
        print("Ok. Continuting on")
        return
    if answ == "exit":
        print("Exiting!")
        sys.exit()


create_folder()
pyenv_options()
pyenv_local_options()
pip_install()
print("project has been initated!")
