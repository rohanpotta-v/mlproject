from setuptools import find_packages,setup #this will find all the package the ML prooject needs
from typing import List
def get_requirements(file_path:str) ->List[str]:
    '''
    This fucntion will return the lust of all the requirements of packages
    '''
    HYPHE_E = '-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

    if  HYPHE_E in requirements:
        requirements.remove(HYPHE_E)
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='Rohan',
    author_email='Rohan.potta@veltris.com',
    packages=find_packages(), #This is able to find all the packages by having the __init__.py file in every directory
    # install_requires=['pandas','numpy','seaborn'] #This will install all the packages required but that is already taken care by requirements.txt
    install_requires=get_requirements('requirements.txt')

)