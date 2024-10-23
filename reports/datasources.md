
# Datasources

Research question: Identify and evaluate publicly available Covid-19 datasets that can complement the primary dataset.


## Research Objectives and Data Requirements

The objective is to find supplementary datasets that can:

1. Enrich our existing Covid-19 data through **additional features and variables**
2. Improve both **model performance and explainability** by incorporating relevant **contextual data** (e.g., demographic factors, social indicators, healthcare infrastructure)
3. Enable **new analytical perspectives and insights**
4. Support robust **cross-validation** through independent data sources


### Evaluation criteria

The datasets should ideally provide value in one or more of these areas. (In an applied project, further criteria like regular updates would also be relevant). In this exploratory phase, we will evaluate potential datasets based on:

Primary criteria:

1. License and availability (focus on open data)
1. Data format and accessibility
1. Documentation quality and metadata
1. Number of observations and variables
1. Temporal and geographical coverage
1. Level of aggregation (individual cases, regional, national)

Secondary:

1. Data collection methodology
1. Known limitations or biases
1. Compatibility with our primary dataset
1. Potential for feature engineering
1. Community adoption and citations in research

Note: While aspects like update frequency would be crucial for deployment scenarios, our focus is on establishing potential value for analysis and modeling experiments.


### Data Resource Categories

During the search for complementary dataset, severaul main categories became apparent. The following classification considers both data types and domains, and is meant to guide a systematically evaluation of potential data sources. Naturally, these categories are not mutually exclusive, and individual datasets may fit multiple categories or subcategories.

1. **Data Hubs and Repositories**: Official collections, open data initiatives, research databases or research repositories

1. **Clinical and Diagnostic Imaging Data**: CT, MRT, X-ray images (primarily lungs of Covid-19 patients)

1. **Genomic Data**: SARS-CoV-2 genome sequences; proteoimcs

1. **CCase-Level Clinical Data**: individual patient records, described by
   * Content: disease progression, outcomes, clinical details (laboratory, comorbidities, medication, treatments, ...)
   * Type:
     * Cross-sectional data (single time point, e.g., admission or discharge)
     * Longitudinal/time series data (multiple observations per patient)
     * Event-based data (specific medical events, interventions)
     * Cohort studies (defined groups followed over time)
     * Registry data (systematic collection of routine clinical data)
     * Emergency department, ICU (high-frequency measurements)
     * Post-discharge follow-up data
     * Linked data (connecting different data sources per patient)

1. **Epidemiological Time Series**: aggregated statistics, rates
   * Events: infection, recovery, hospitalization, ICU, deaths, long covid
   * Activities: testing, vaccination

1. **Healthcare System Data**
   * Hospital and ICU availability/resources
   * Healthcare workforce statistics

1. **Policy and Intervention Data**: lockdowns, vaccination programs, mask mandates, travel restrictions

1. **Survey Data**: representative population samples (socio-economic, demographic, health behaviour)

1. **Alternative Data Sources**
   * (a) Social media trends
   * (b) Search engine patterns
   * (c) Mobility data
   * (d) News coverage

1. **Software, Models and Applications**
   * (a) Public models (prediction, simulation)
   * (b) Software packages (R, python)
   * (c) Interactive dashboards and visualizations

1. **Scientific Publications**
   * (a) Meta-papers about Covid-19 data resources and repositories
   * (b) Research papers with accompanying data/code
     * Epidemiological analyses
     * Clinical and/or intervention studies
   * (c) Literature reviews and meta-analyses
   * (d) other related publications

1. **Other**
   * (a) Environmental Data: air quality, weather
   * (b) Demographics and population
   * (c) Economic: economics, employment


### Search Strategy

The search for complementary datasets follows an iterative approach, ranging from well-known data hubs and repositories, through systematic searches in scientific databases and data catalogs, to broader explorations using established search engines. Given the exploratory nature of this first iteration, we focus on highly selected, most promising, frequently cited and well-documented resources (following the Pareto principle, where roughly 20% of the sources might provide 80% of the value).

Initial searches combine Covid-19 related terms (e.g., "SARS-CoV-2", "COVID-19", "coronavirus") with specific data types and domains as outlined in the categorization (e.g., "epidemiology", "clinical", "case-level", "genetic", "genome"). Furthermore, terms from the reference dataset (e.g., "Mexico") are considered. Resources that have been active since 2020 and are still or at least recently maintained or concluded with a complete dataset are the main focus. The search includes both general-purpose platforms (like Kaggle, GitHub, Google Dataset Search, Zenodo) and specialized repositories (medical, epidemiological databases, national health institutes).

The search and documentation process is conducted in multiple phases:

1. Initial exploration following the described strategy to quickly scan the possible solution space. Results are collected as a simple link collection rather than detailed documentation with "Data Resource Cards".
2. Based on these findings, the strategy is further specified and the presented categorization is developed. The discovered resources are roughly sorted and evaluated regarding their relevance and potential utility. The resulting list is presented in the "Interim Results" section.
3. Finally, the most promising resources are documented exemplarily using "Data Resource Cards".

For a more comprehensive or systematic approach, methods related to structured literature reviews in the domain of Health Technology Assessments (HTA) would be highly advisable. The clear definition of search terms, inclusion and exclusion criteria, and structured frameworks like PICO (Population, Intervention, Comparison, Outcome) would facilitate a more systematic and professional approach.

The following aspects require further specification for a more systematic approach:

* Search methodology and detailed documentation of search paths
* Systematic combinations of search terms
* Complete list of searched platforms and databases
* Specific timeframe requirements
* Formal inclusion/exclusion criteria


### Project Context

[ToDo]?

* Brief description of the primary dataset
* Current modeling approach
* Specific challenges or limitations we're trying to address


### Resource Assessment Process

The evaluation of data resources should be guided by a systematic approach to ensure consistent results. While the *Data Resource Card*s and *Data Resource Categories* allow to describe all kind of results, only a sample of the most promising resources is documented in the first iteration.

For further iterations and a more professional approach, the following aspects need to be refined:

* **Application of Evaluation Criteria**: Currently, criteria are applied informally during initial screening. A more structured approach would require specific thresholds, weights, and documentation of the evaluation process.

* **Rating System**: The current 0-5 scale provides initial guidance but would benefit from specific definitions and examples for each level (or even calibration sessions to ensure consistent ratings).

* **Review Process**: While the initial screening is conducted individually, a formal review process including cross-validation, regular team reviews, and systematic documentation of decisions would enhance reliability.



### Data resource documentation

While there are established tools and platforms for managing and documenting data resources (research data repositories such as CKAN, DataCite), we opt for a simpler approach suitable for our exploratory project. The following template provides a structured way to document relevant information about each identified data source, enabling systematic documentation, evaluation and comparison.

Each data resource card captures key characteristics, quality aspects, and potential applications in our context.

```markdown

## Title/Name

**Basic Information**
* Title/Name:
* URL/URI:
* Rating (0-5): 5
* Categories: [references to category numbers]
* Last Updated:

**Description**

Brief description of the resource...

**Content**
* Key variables:
* Sample size:
* Time period:
* Geographic coverage:

**Technical Details**
* Format:
* Access method:
* License:
* Documentation quality:
* Relationships to other resources: [part of; related to; referenced by; provided by]

**Quality Assessment**

_Primary Criteria_ \
[List ratings/comments for each primary criterion]

_Secondary Considerations_ \
[List ratings/comments for each secondary criterion]

**Potential Applications**
* Use case 1:
* Use case 2:
* Integration notes:

**Additional Notes**
* Limitations:
* Special considerations:

- - - - - - - - - -
```


# Intermediate results

## Kaggle

* https://www.kaggle.com/datasets?tags=16575-Coronavirus
  * https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge
  * https://www.kaggle.com/datasets/arashnic/covid19-case-surveillance-public-use-dataset/code \
  --> CDC
  * https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database
  * https://www.kaggle.com/datasets/pushkar007/covid-deeppredictor
  * https://www.kaggle.com/datasets/josetroyatoscano/covid19-colombia-complete-dataset-dec-2023


## Genome

* https://github.com/albertotonda/deep-learning-coronavirus-genome/tree/master
* https://www.kaggle.com/code/mlconsult/covid-19-genome-variations/notebook

## XRay

* https://github.com/ieee8023/covid-chestxray-dataset

## Literature

* https://pmc.ncbi.nlm.nih.gov/articles/PMC8083224/

## other

* https://www.covid19dataportal.org/
* https://researchguides.library.tufts.edu/c.php?g=905212&p=8319620
* https://aimi.stanford.edu/covid-19-testing-page#data
* https://data.world/resources/coronavirus/
* https://opendatawatch.com/whats-being-said-resource/data-in-the-time-of-covid-19/
* https://hsls.libguides.com/health-data-sources/data-sets
  * https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf/about_data
  * https://data.cdc.gov/Vaccinations/COVID-19-Vaccination-Demographics-in-the-United-St/km4m-vcsb/about_data
  * !! https://radxdatahub.nih.gov/studyExplorer?&sort=desc&prop=relevance&page=1&size=50
* https://datacatalog.worldbank.org/search?q=covid&start=0&sort=
  * https://datacatalog.worldbank.org/search/dataset/0063588/Mexico---Socioeconomic-Impact-of-COVID-19--2021

CDC 

* https://data.cdc.gov/browse?limitTo=datasets&tags=covid-19&sortBy=most_accessed&utf8=%E2%9C%93
  * https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf
  * https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t/about_data
  * https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4/about_data
    * https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4/data

### Google

* https://health.google.com/covid-19/open-data/raw-data
* https://datasetsearch.research.google.com/search?query=coronavirus+covid-19&docid=L2cvMTFranE1eXFrOQ%3D%3D
* https://github.com/GoogleCloudPlatform/covid-19-open-data/blob/main/docs/table-search-trends.md

## Survey, Public statistics

* https://www.health.govt.nz/statistics-research/surveys/access-to-survey-microdata
* https://www.data.gv.at/daten/covid-19/
* https://www.pathogens.se/datasets/public-health/
* https://covid19ireland-geohive.hub.arcgis.com/

## R

* https://kjhealy.github.io/covdata/articles/covdata.html
* https://cran.r-project.org/web/packages/covid19.analytics/vignettes/covid19.analytics.html
* http://www.repidemicsconsortium.org/
* https://covid19datahub.io/index.html
* https://rviews.rstudio.com/2021/12/08/the-r-package-covid19/
* https://mine-cetinkaya-rundel.github.io/covid19-r/
* https://github.com/joachim-gassen/tidycovid19

## Python

* https://github.com/alvarobartt/covid-daily


# Data Resource Cards

## CDC: COVID-19 Case Surveillance Public Use Data with Geography

**Basic Information**

* Title/Name: COVID-19 Case Surveillance Public Use Data with Geography
* URL/URI: https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Geo/n8mc-b4w4
* Rating (0-5): 5
* Categories: Case Surveillance, Public Health
* Last Updated: July 9, 2024 (Data), July 17, 2024 (Metadata)

**Description**
Comprehensive individual-level COVID-19 case surveillance data reported to CDC by U.S. states and territories. Contains 19 key data elements including demographics, geography, exposure history, disease severity indicators, outcomes, and underlying conditions.

**Content**

* Key variables: Case month, location (state/county), demographics, disease severity, outcomes, exposure history, underlying conditions
* Sample size: 106 million records
* Time period: January 2020 - July 5, 2024
* Geographic coverage: United States (state and county level)

**Technical Details**

* Format: Structured dataset
* Access method: Direct download or API access through data.cdc.gov
* License: Public Domain U.S. Government
* Documentation quality: Excellent - comprehensive data dictionary and methodological documentation
* Relationships: Part of CDC COVID-19 response data collection; Related to other CDC COVID-19 datasets

**Quality Assessment**

_Primary Criteria_

* Completeness: High - covers all U.S. jurisdictions
* Accuracy: High - follows standardized case definitions and reporting protocols
* Timeliness: Monthly updates with 14-day reporting lag
* Documentation: Excellent - detailed metadata and methodological documentation

_Secondary Considerations_

* Data suppression for privacy protection
* Dynamic nature of case reporting with possible updates to historical data
* Variable reporting compliance across jurisdictions

**Potential Applications**

* Epidemiological analysis of COVID-19 patterns and trends
* Health equity research examining demographic disparities
* Public health response evaluation and planning
* Integration with other health and socioeconomic datasets

**Additional Notes**

* Limitations:
  - Reporting discontinued after July 1, 2024
  - Some jurisdictions stopped reporting after May 2023
  - Data suppression may limit certain analyses
  - Known issues with Texas death reporting

* Special considerations:
  - Data are provisional and subject to updates
  - Privacy protections affect certain demographic combinations
  - Regular quality assurance procedures applied by CDC

**References**

* similar datasets (without Geography) available at kaggle ([Covid-19 Case Surveillance Public Use Dataset](https://www.kaggle.com/datasets/arashnic/covid19-case-surveillance-public-use-dataset/data]))


## Google COVID-19 Search Trends Symptoms Dataset

**Basic Information**
* Title/Name: COVID-19 Search Trends Symptoms Dataset
* URL/URI: 
  - https://console.cloud.google.com/marketplace/product/bigquery-public-datasets/covid19-search-trends
  - https://github.com/GoogleCloudPlatform/covid-19-open-data/blob/main/docs/table-search-trends.md
* Rating (0-5): 4
* Categories: Search Trends, Symptom Surveillance
* Last Updated: Feb 24, 2021 (dataset ended)

**Description**
Aggregated, anonymized trends in Google searches for health symptoms, signs, and conditions, providing daily or weekly time series showing relative search volumes by region. Dataset is privacy-protected using differential privacy techniques.

**Content**

* Key variables: Region, date, normalized search volumes for various symptoms
* Sample size: Coverage of Google Search users in included regions
* Time period: 2020-2021 (ended Feb 2021)
* Geographic coverage: Initially US, later expanded to Australia, Ireland, New Zealand, Singapore, and UK

**Technical Details**

* Format: BigQuery tables, CSV files
* Access method: Google BigQuery, direct CSV download
* License: Google Terms of Service
* Documentation quality: Excellent - comprehensive methodology documentation
* Relationships: Part of Google's COVID-19 Public Dataset Program, related to COVID-19 Open-Data repository

**Quality Assessment**

_Primary Criteria_

* Completeness: High within covered regions
* Accuracy: Uses differential privacy, normalized data
* Timeliness: Was updated weekly (now discontinued)
* Consistency: Standardized processing across regions

_Secondary Considerations_

* Privacy-preserving noise addition
* Multiple temporal resolutions (daily/weekly)
* Region-specific scaling factors
* Multi-language support within regions

**Potential Applications**

* Early detection of COVID-19 outbreaks
* Public health surveillance
* Behavioral response analysis
* Integration with clinical data for validation

**Additional Notes**

* Limitations:
  - Dataset discontinued
  - Cannot compare across regions
  - Represents only Google Search users
  - Added noise for privacy protection

* Special considerations:
  - Different scaling factors by region
  - Weekly values available in two forms (direct and aggregated from daily)
  - Search queries can map to multiple symptoms
  - Not intended for medical diagnosis or personal guidance



## Title/Name

**Basic Information**

* Title/Name: 
* URL/URI:
* Rating (0-5): 5
* Categories: [references to category numbers]
* Last Updated:

**Description**

Brief description of the resource...

**Content**

* Key variables:
* Sample size:
* Time period:
* Geographic coverage:

**Technical Details**

* Format:
* Access method:
* License:
* Documentation quality:
* Relationships to other resources: [part of; related to; referenced by; provided by]

**Quality Assessment**

_Primary Criteria_ \
[List ratings/comments for each primary criterion]

_Secondary Considerations_ \
[List ratings/comments for each secondary criterion]

**Potential Applications**

* Use case 1:
* Use case 2:
* Integration notes:

**Additional Notes**

* Limitations:
* Special considerations:

- - - - - - - - - -