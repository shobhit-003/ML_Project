from setuptools import find_packages, setup
# No need to write "setuptools" dependancy in req.txt as its by default present
# "find_packages" will search for every package (__init__.py) in source directory
# package is nothing but __init__.py file

from typing import List                     
# if we don't give data type in python then by default it gives data type to variable
# it's good to give data type by ourself to avoid any ambiguity, either in the func argument and in its return type
# these are just hints for someone that it should be the data type
# python doesn't throw an error if data type mismatch like C++ i.e. python doesn't force data type at run time

HYPEN_E_DOT = '-e .'
def get_requirements(file_path : str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] # to remove "enter (\n) from req.txt"

        if HYPEN_E_DOT in requirements: # to remove '-e .' bcoz its not a dependancy, its a command to create package
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name = 'mlproject',
    version = '0.0.1',
    description = "first end to end project",
    author = "shobhit",
    author_email = "shobhitgpt28@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)

# we can create install_requires = ['numpy', 'pandas'] in this way also but then its not feasible
# hence we created get_requirements func, now we have to write depedancy in req.txt file only