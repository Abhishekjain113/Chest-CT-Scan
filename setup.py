from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def gets_requirements(filepath:str)->List[str]:
    req=[]
    with open(filepath) as file_obj:
        req=file_obj.readline()
        req=[reqq.replace('\n','') for reqq in req]
        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
        return req
    

setup(
    name="CT scan Chest",
    version='0.0.1',
    author='abhishek jain',
    author_email='jainabhishek1115@gmail.com',
    install_require=gets_requirements('requirement.txt'),
    packages=find_packages()
)