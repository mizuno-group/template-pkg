import os
import re
from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

# modify entry_points to use command line 
# {COMMAND NAME}={module path}:{function in the module}
setup(
    name="template-pkg", # 変更する
    version="0.0.1", # 変更する
    description="a template for CLI package", # 変更する
    author="tadahaya", # 変更する
    packages=find_packages(),
    install_requires=install_requirements,
    include_package_data=True, # necessary for including data indicated in MANIFEST.in
    entry_points={
        "console_scripts": [
            "mypkg=mypkg.core:main", # 変更する
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.10', # 変更する
    ]
)