# Python Virtual Environment & PIP

## What is a Virtual Environment?

a virtual env is a private workspace for a python project it can install its own packages,dependencies,can have its own settings in that workspace (virtual env) independent of our computer and the other python projects

- Imagine we have two Python projects.
  - Project A needs:
    • Package X version 1.0

  - Project B needs:
    • Package X version 2.0

- agr hum in dono versions ko globally apny computer par install krty hain to ye conflict kar skty
- virtual env is problem ko solve krta h by creating seprate wrk place for each project
- we will have virtual env A and virtual env B for both projects
- now both projects are independent of each other

### Without a virtual environment:

- all the projects share same packages
- updating a package for one project can break the other project

### With a virtual environment:

- each project will have its own packages
- projects will not interfere with each other
- we can safely experiment and instakll anything we need

# Creating a Virtual Environment

- python k pass built-in venv module h to create virtual environments
- to cretae virtual env open command prompt navigate to the folder where you want to create it and then run following command to create the virtual env
  - python -m venv envname
- -m means module
- we can see the results in virtual env folder (myfirstproject)

# Activate Virtual Environment

- to use virtual env we need to activate it frst using following command
- envname\Scripts\activate
- After activation, your prompt will change to show that you are now working in the active environment
- Scripts contains:
  • activate command files

  ### command files : Small executable files that run commands like activate, python, and pip inside the virtual environment.

  • Python executable for that venv
  • pip for installing packages

- So this command:
  myfirstproject\Scripts\activate

- means:
  • go inside the venv folder
  • open Scripts folder
  • run the activate script
- What other folders do:

  • Lib/
  Stores installed packages. No activation logic.

  • pyvenv.cfg
  Stores configuration only.

# PIP

- pip is python's package manager
- it installs external libraries
- it works in virtual env or globally (both)
- examples :numpy,pandas,cowsays

- baisc idea
  - hum ny command likhi
  - pip library ko download aor install kry ga
  - hum library ko code main import kren gy or use kren gy

# Install Packages/libraries

- once the virtual env is activated now we can install packages /libraries in our project using pip
- pip install library_name

# Using Package

- after installing finished just import the library and start using it

# Deactivate Virtual Environment

- to deactiavte the virtual env just run the following command
  - deactivate
- As a result, we will be now back in the normal command line interface

### why we usually feel need to decativate virtual env?

- once we finish working on a projeect we can deactivate it
- so that we stop using that project's python
- avoid confusions ,avoids installing or running things in the wrong environment

### then what if we have to wrk in that project again??

- we can activate that same virtual env again bcz it stya there until we delte it

# Delete Virtual Environment

- Another nice thing about working with a virtual environment is that when we, for some reason want to delete it, there are no other projects depend on it, and only the modules and files in the specified virtual environment are deleted

- use following command to dlete a venv
  - rmdir /s /q virtualenvname
  - rmdir = remove directory, it deletes a folder
  - /s = delete the folder and everything inside it
  - /q = quiet mode, no confirmation prompts
- virtualenvname = the folder name you want to delete

### why we need to delte the virtual enviromnet

We delete virtual environments because they are just temporary project setups that can be recreated anytime.

# extras:

- run dir to see foldrs/files list
- run cd to see current location
- cd folder name to navigate
