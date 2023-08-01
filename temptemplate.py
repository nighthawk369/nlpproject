import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,filemode='w',filename='application.log',format='%(asctime)s - %(levelname)s - %(message)s')

projectName='text_summerizer'

fileNames=[
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/utils/common.py",
    f"src/{projectName}/login/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for name in fileNames:
    name=Path(name)
    dir,fname=os.path.split(name)
    # print(dir)
    print(fname)

    # if dir == "":
    #     os.mkdir(dir,exist_ok=True)
    # elif 
    

