from setuptools import find_packages,setup
from typing import List



def get_requirements{file_path:str}->List[str]:
    '''
    this function retuns list
    '''

    requiremets=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements] 

        if HYPEN_E_DOT in requiements:
            requirements.remove(HYPEN_E_DOT)    

    return requirements        



name='Ds projects',
version='0.0.1',
author='Sai',
author_email='banteshravani@gmail.com',
packages=find_packages(),
install_requires=get_requirements("requirement.txt")


)