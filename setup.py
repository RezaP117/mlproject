# building application as a package 

# automatically finds all packages used in project
from setuptools import find_packages, setup
from typing import List 

# used for parsing requirements file and getting all external libraries used 
# takes in a file path string and returns a list of strings 
# "-e ." in requirements.txt automatically starts setup.py  

E_FLAG = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj: 
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] 
        
    if E_FLAG in requirements: 
        requirements.remove(E_FLAG)
    return requirements 

# meta data information about project 
# find packages will check where __init__.py file(s) are in the directory  
setup(
    name = "mlproject",
    version = "0.0.1", 
    author = "Reza", 
    author_email = "rezaknpasha@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)
