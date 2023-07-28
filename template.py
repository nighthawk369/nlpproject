import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

projectname="textsummerizer"

list_files = [".github/workflows/.gitkeep",
              f"src/{projectname}/__init__.py",
              f"src/{projectname}/components/__init__.py",
              f"src/{projectname}/utils/__init__.py",
              f"src/{projectname}/utils/common.py",
              f"src/{projectname}/login/__init__.py",
              f"src/{projectname}/config/__init__.py",
              f"src/{projectname}/config/configuration.py",
              f"src/{projectname}/pipeline/__init__.py",
              f"src/{projectname}/entity/__init__.py",
              f"src/{projectname}/constants/__init__.py",
              "config/config.yaml",
              "params.yaml",
              "app.py",
              "main.py",
              "Dockerfile",
              "requirements.txt",
              "setup.py",
              "research/trials.ipynb"
              ]

for loc in list_files:
    loc=Path(loc)
    dir,fi=os.path.split(loc)
    logging.info(f"Splitting directory {dir} and files {fi}")    
    if dir != "":
        os.makedirs(dir, exist_ok=True)
        logging.info(f"Created directory {dir} for file {fi}")
    if (not os.path.exists(loc)) or (os.path.getsize(loc) == 0):
        with open(loc,"w") as f:
            pass
        logging.info(f"Created empty file {loc}")
    else:
        logging.info(f"File {loc} already exists")