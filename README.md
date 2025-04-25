# BSDA Capstone Project
# Socioeconomic Factors Impacting Poverty in U.S. Counties: A Regression Approach

## Project Overview
This project aims to apply multiple linear regression to analyze the influence of socioeconomic factors on poverty rates across U.S. counties.

**Research question:** What is the relative importance of each socioeconomic factor in explaining poverty rates in U.S. counties, and how well can we predict poverty rates based on these factors using multiple linear regression?

## Prerequisites
- Jupyter Notebook
- Python with the following libraries:
  - requests
  - json
  - pandas
  - numpy
  - statmodels
  - matplotlib
  - seaborn
  - scikit-learn
  - scipy

## Project Files
### Datasets
- The data used for analysis was collected by making API requests to the U.S. Census Bureau.
- 3 JSON files are stored in the project folder to provide variable metadata used in ``retrieving_variable_codes.ipynb``:
    - [b_variables.json](./b_variables.json) was downloaded from [Detailed Tables Variables](https://api.census.gov/data/2023/acs/acs1/variables.json).
    - [s_variables.json](./s_variables.json) was downloaded from [Subject Tables Variables](https://api.census.gov/data/2023/acs/acs1/subject/variables.json).
    - [dp_variables.json](./dp_variables.json) was downloaded from [Data Profiles Variables](https://api.census.gov/data/2023/acs/acs1/profile/variables.json).

### Notebooks
This project's workflow was broken down into 4 notebooks:
- ``retrieving_variable_codes.ipynb``: This notebook retrieves ACS variable codes from variables metadata to assist API request construction.
- ``data_extraction_&_data_wrangling.ipynb``: This notebook covers the process of acquiring and cleaning data.
- ``main_analysis.ipynb``: Main analysis notebook includes EDA, data preparation, model building, model validation, hypothesis testing and visualizations.
  - **Note: Before running this notebook for the first time, ``data_extraction_&_data_wrangling.ipynb`` should be executed once to generate cleaned dataset in the project folder.**
- ``model_refinement_experiments.ipynb``: This notebook explores various model refinement strategies such as transformation testing, interaction term, and robust standard errors.
  - **Note: Before running this notebook for the first time, code in part A of ``main_analysis.ipynb`` should be executed at least once to generate transformed data in the project folder.**

### Documents
- ``Capstone_Proposal.pdf``: Project propsal
- ``Capstone_Report.pdf``: Project report

## Objective & Deliverables
- Objective 1: Data preparation and exploratory data analysis (EDA)
  - Deliverable 1.1: Data retrieval from the U.S. Census Bureau
  - Deliverable 1.2: A cleaned dataset with selected variables and handled missing or inconsistent entries
  - Deliverable 1.3: A summary of EDA including descriptive statistics, correlation analysis and visualizations (pairplots, correlation matrix, regression plots, histograms, boxplots)
  - Deliverable 1.4: Transformed variables to address nonlinearity and skewness, and documented justification for each transformation
- Objective 2: Build and evaluate a baseline multiple linear regression model
  - Deliverable 2.1: An OLS model fitted on transformed and scaled predictors with train/test split
  - Deliverable 2.2: A summary of baseline model performance 
  - Deliverable 2.3: Preliminary interpretation of coefficients and statistical significance
- Objective 3: Perform model diagnostics to validate model assumptions 
  - Deliverable 3.1: Residual plots (residuals vs. fitted values, residuals vs. predictors) to assess homoscedasticity and linearity 
  - Deliverable 3.2: Histogram, boxplot and Q-Q plot of residuals to assess normality 
  - Deliverable 3.3: A summary of baseline model validity and limitations
- Objective 4: Refine the regression model to improve reliability and account for identified issues. 
  - Deliverable 4.1: A new multiple linear regression model that incorporates improvements such as variable transformation, interaction term, and robust standard errors (HC3).
  - Deliverable 4.2: A summary of updated model performance metrics 
  - Deliverable 4.3: Statistical output including hypothesis test results (F-test and t-tests)
  - Deliverable 4.4: A summary of the relative importance of predictors, including a tornado diagram of standardized coefficients
  - Deliverable 4.5: Revised model diagnostics with visualizations to confirm improvements in model assumptions
- Objective 5: Present results and communicate findings
  - Deliverable 5.1: A written project report summarizing methodology, findings, and conclusions
  - Deliverable 5.2: At least one well-documented Jupyter Notebook with code, outputs, and narrative explanations
  - Deliverable 5.3: A video presentation explaining the project process, results, and insights
