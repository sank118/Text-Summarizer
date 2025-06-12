import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name="textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # Initialize the package
    f"src/{project_name}components/__init__.py", # Initialize the components package
    f"src/{project_name}/utils/__init__.py", # Initialize the utils package
    f"src/{project_name}/utils/common.py", # Common utility functions
    f"src/{project_name}/logging/__init__.py", # Initialize the logging package
    f"src/{project_name}/config/__init__.py", # Initialize the config package
    f"src/{project_name}/config/configation.py", # Configuration management
    f"src/{project_name}/pipelines/__init__.py", # Initialize the pipelines package
    f"src/{project_name}/entity/__init__.py", # Initialize the entity package
    f"src/{project_name}/constants/__init__.py", # Initialize the constants package
    "config/config.yaml", # Configuration file
    "parameters.yaml", # Parameters file
    "app.py", # Main application file
    "main.py", # Entry point for the application
    "requirements.txt", # List of dependencies
    "Dockerfile", # Dockerfile for containerization
    "research/trials.ipynb", # Jupyter notebook for experimentation
    "setup.py" # Setup script for the package
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            logging.info(f"Creating an emptyfile: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")

