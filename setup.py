'''
This is setup file to define the configurations of the project, such as metadata, dependencies.

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This will get list of requirements 
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst
    
print(get_requirements())

setup(
    name ="NetworkSecurity",
    version="0.0.1",
    author="Dhruv Gupta",
    author_email="dhruv072020@hmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)