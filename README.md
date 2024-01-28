Cric-Stats-Analytics
====================

Analyse cricketers' performance using NLP on live commentary data and scorecard:
* This would help in making a useful and less biased interpretation of performances and  phases of play. 
* Use statistics and analytics and come up with meaningful metrics to gauge and rate performances.

# Requirements
* Python 3.10+
* Dependency management using poetry

# Project Structure
```
Cric-Stats-Analytics
|--notebooks/           # jupyter notebooks for explorations
|
|--data/                # data for project
|
|--models/              # data-models used for project
|
|--src                  # source-code
|   |--extract_data/      # extract raw-data from data-file for analysis
|   |--prepare_data/      # prepare data for analysis
|   |--pre_analysis/      # descriptive analysis of data
|   |--final_analysis/    # final analysis including regression/modelling
|
|--main.py              # entry-point into codebase
|--README.md        
|--.gitignore
|--pyproject.toml
|--poetry.lock

```
# Usage
## Environment setup
We use poetry for setting up interpreter and environment. Ensure that poetry is installed on machine.

* To install poetry using `pipx`
```shell
pipx install poetry
```
* Switch to/create environment for current project.
```shell
poetry shell
```
* Install dependencies using poetry
```shell
poetry install
```

* To run code in the project
```shell
python main.py
```

# Background information