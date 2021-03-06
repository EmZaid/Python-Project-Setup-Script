#! /Users/Emilienne/.pyenv/shims/python
"""This is a script to set up a new python project"""

import os
import subprocess
import sys
import argparse
from pathlib import Path


# Refactoring to use argparse
parser = argparse.ArgumentParser()

parser.add_argument(
    "-a",
    "-all",
    dest="all",
    help="Runs full script, minimal interaction possible depending on argumenst passed.",
    action="store_true",
)
parser.add_argument(
    "-n", "-name", dest="name", type=str, help="Input your project name"
)


parser.add_argument(
    "--path",
    type=lambda p: Path(p).absolute(),
    default=os.getcwd(),
    help="Path to the python project directory",
)

args = parser.parse_args()


# Checks to make sure a project name was provided. If not, prompt user for one.
if not args.name:
    project_name = input("Project Name:")
else:
    project_name = args.name


PROJ_DIR = str(args.path)
new_proj_path = PROJ_DIR + "/" + project_name + "/"


def create_folder():
    """This will create a new project in Python Projects"""

    try:
        os.mkdir(new_proj_path)
    except OSError:
        print(
            f"Creation of the directory {project_name} failed. Directory probably alreadly exists. Exiting"
        )
        sys.exit()
    else:
        print(f"Successfully created the directory {project_name}")


def pyenv_options():
    """This gives the user options about creating a virutalenv"""

    if not args.all:
        accepted_answ = ["y", "n", "exit", "yes", "no"]
        yes_answ = ["y", "yes"]
        no_answ = ["n", "no"]

        answ = input("Do you want to create a new virtualenv? y/n/exit:")
        answ = answ.lower()

        while answ not in accepted_answ:
            answ = input("please enter: \ny/n/exit:")
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
    elif args.all:
        subprocess.run(["pyenv", "virtualenv", project_name], check=True)
        return


def pyenv_local_options():
    """lets you create a .python-version file"""
    if not args.all:
        accepted_answ = ["y", "n", "exit", "yes", "no"]
        yes_answ = ["y", "yes"]
        no_answ = ["n", "no"]

        # This file, assuming you set up pyenv
        answ = input("Do you want to set up a .python-version file? \n y/n/exit:")
        answ = answ.lower()

        while answ not in accepted_answ:
            answ = input("please enter: \ny/n/exit:")
            answ = answ.lower()
        while answ in yes_answ:
            print("Ok. Creating .python-version now:")
            os.system("echo " + project_name + ">>" + new_proj_path + ".python-version")
            return
        while answ in no_answ:
            print("Ok. Continuting on")
            return
        if answ == "exit":
            print("Exiting!")
            sys.exit()
    elif args.all:
        os.system("echo " + project_name + ">>" + new_proj_path + ".python-version")


def pip_install():
    """installs black, pylint, and a .pylintrc file"""
    if not args.all:

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
                "~/.pyenv/versions/"
                + project_name
                + "/bin/python -m pip install black pylint"
            )

            os.chdir(new_proj_path)
            with open(".pylintrc", "w", encoding="UTF-8") as outfile:
                subprocess.run(
                    ["pylint", "--generate-rcfile"], check=True, stdout=outfile
                )

            return
        while answ in no_answ:
            print("Ok. Continuting on")
            return
        if answ == "exit":
            print("Exiting!")
            sys.exit()

    elif args.all:
        os.system(
            "~/.pyenv/versions/"
            + project_name
            + "/bin/python -m pip install black pylint"
        )
        os.chdir(new_proj_path)
        with open(".pylintrc", "w", encoding="UTF-8") as outfile:
            subprocess.run(["pylint", "--generate-rcfile"], check=True, stdout=outfile)


if __name__ == "__main__":
    create_folder()
    pyenv_options()
    pyenv_local_options()
    pip_install()
    print("Project has been initated!")
