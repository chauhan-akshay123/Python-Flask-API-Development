# Python-Flask-API-Development

# Flask Project Setup Instructions

## Introduction

This guide explains how to set up a Flask project using a virtual environment to manage dependencies. 

---

## Steps to Set Up the Project

### 1. Create a Virtual Environment
A virtual environment is used to isolate dependencies for this particular project and prevent conflicts with globally installed Python dependencies.

Run the following command in the terminal:
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment
After creating the virtual environment, activate it using the command: 
```bash
venv/Scripts/activate
```
### 3. Install Flask
Once the virtual environment is activated, install Flask by running:
```bash
pip install Flask
```
### 4. Document Project dependencies
To document all the packages and dependencies used in the project, run the following command
```bash
pip freeze > requirements.txt
```
This will generate a `requirements.txt` file containing all installed dependencies.

### 5. To run
To run the application, use following command in the terminal: 
```bash
python <file_name>.py 
```


