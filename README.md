# covid-19-risiko-erkennung

Analyse und Modellierung von Covid-19 Risikofaktoren im Rahmen des Projektpraktikums Web Science im Wintersemester 2024 an der Fernuni Hagen.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`


```

--------

## Setup

### Cloning the Repository

Download the repository using git:

```bash
git clone <repository-url>
cd covid-19-risiko-erkennung
```

### Setting Up the Virtual Environment

Set up and activate the virtual environment:
```bash
# Run the setup script to create the virtual environment
src/setup_venv.sh

# Activate the virtual environment
source venv/bin/activate
```
### Kaggle Data Access

To access data from Kaggle, authenticate your Kaggle account:

1. Go to your Kaggle account settings and create a new API token. This will download a kaggle.json file with your credentials.
2. Place the kaggle.json file in the ~/.kaggle/ directory on your system.
