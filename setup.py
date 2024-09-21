from setuptools import find_packages,setup
from typing import List

E_DOT= '-e .'

def get_requires(file_path:str)->List[str]:
    
    '''will input file_path and Returns a list of strings'''
    
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements
        
setup(
    name='mlproject',
    version='0.0.1',
    author='akshay',
    author_email='akshaypdeshpande10@gmail.com',
    packages=find_packages(), # it looks for the following packages in the __init__.py file
    install_requires=get_requires('requirements.txt'),
    
)