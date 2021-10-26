# {{cookiecutter.project_name}}
A short description of the project.

## New Installation 
```bash
# create virtual environment
mkvirtualenv -p python3 -r requirements.txt {{cookiecutter.project_name}}

# activate the environment
workon {{cookiecutter.project_name}}
```

## Project Organization
    ├── README.md          <- The top-level README for developers using this project.
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.