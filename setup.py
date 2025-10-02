from setuptools import find_packages,setup #(to find out the packages which we created for machine learning application)

from typing import List

HYPEN_E_DOT="-e ."
def get_req(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


    
setup(
name="MLproject",
version="0.0.1" , #whatever update will come it will change automatically
author="KaranRK",
author_email="karanrathodkr253@gmail.com",
packages=find_packages(),
insatll_requires=get_req("requirements.txt"),
)