# Predicting Online Purchase Behaviour from Website Engagement

## Contributors
- Aidan Aimy 
- Adrian Chan
- Yujia Huang
- Renata Lovette

---
# Abstract

This project investigates whether website engagement metrics can predict whether an online visitor will complete a purchase on an e-commerce website. Specifically, we examine behavioural indicators such as the number of pages visited, time spent on different types of pages, and website engagement metrics such as bounce rate and exit rate.

Using the **Online Shoppers Purchasing Intention Dataset**, we perform exploratory data analysis and build a classification model using logistic regression to determine whether website activity patterns can predict whether a visitor will generate revenue for the website.

In addition to addressing this research question, this project emphasizes **reproducible data science practices**, including version control using GitHub, literate programming using Jupyter notebooks, and containerized computational environments using Docker.

---

## Research Question

**Can website engagement metrics (such as page visits, time spent on pages, and bounce rate) predict whether an online visitor will make a purchase?**

---

## Dataset

The dataset used in this project is the **Online Shoppers Purchasing Intention Dataset**, which contains information about user behaviour during online shopping sessions.

Dataset source:

https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset

Direct dataset file:

https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv

The dataset includes information about user browsing behaviour during e-commerce sessions. Key variables include:

- **Administrative** – number of administrative pages visited  
- **Administrative_Duration** – time spent on administrative pages  
- **Informational** – number of informational pages visited  
- **Informational_Duration** – time spent on informational pages  
- **ProductRelated** – number of product-related pages visited  
- **ProductRelated_Duration** – time spent on product-related pages  
- **BounceRates** – proportion of visitors leaving after viewing a page  
- **ExitRates** – proportion of exits from a page  
- **PageValues** – average value of a page before a purchase  
- **SpecialDay** – proximity to special shopping days (e.g., holidays)

Additional categorical variables include:

- Month
- OperatingSystems
- Browser
- Region
- TrafficType
- VisitorType
- Weekend

The target variable used in this project is:

**Revenue**

```
TRUE  → the visitor completed a purchase  
FALSE → the visitor did not complete a purchase
```

This makes the task a **logistic regression problem**.

---

# Methods Overview

The analysis will follow the typical stages of a data science workflow:

1. **Data Loading**  
   Import the dataset from the original source.

2. **Data Cleaning and Wrangling**  
   Prepare the dataset by handling missing values and formatting variables appropriately.

3. **Exploratory Data Analysis (EDA)**  
   Summarize the dataset and create visualizations to understand relationships between online activity and shopping behaviour.

4. **Predictive Modeling**  
   Build a logistic regression model to predict shopping preference based on online activity and demographic features.

5. **Model Evaluation**  
   Evaluate the model's performance using appropriate metrics such as accuracy and confusion matrices.

---

# Project Summary

This project used logistic regression to predict whether online visitors would complete a purchase based on browsing behaviour metrics like page visits, duration, and bounce rates. The model achieved 87.8% accuracy but struggled to identify actual purchasers due to class imbalance, which was partially addressed through class weighting. Results confirm that engagement metrics carry meaningful predictive signal; features related to browsing activity appear to capture patterns associated with purchasing behaviour, even when using a relatively simple logistic regression model. Future work could improve predictive performance through implementingmore advanced models, resampling techniques, and richer feature sets that captures a more holistic insight into customer behaviours.

---

## Reproducibility

This project emphasizes reproducible data science practices using version control (GitHub), literate programming (Quarto), and containerized environments (Docker).

### Prerequisites

- Docker
- Conda or Miniconda

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/UBC-DSCI-310-2025W2/dsci-310-group-02-team2.git
   cd dsci-310-group-02-team2
   ```

2. Create the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate dsci-310-team2
   ```

3. Build the Docker image:
   ```bash
   docker build -t quarto-env .
   ```

### Running the Analysis

The analysis is implemented in `analysis/online-purchase-prediction.qmd`, a Quarto document that combines code, narrative, and visualizations.

To run the full reproducible pipeline:

```bash
make all
```

This will:
- Clean the raw data (`data/online_shoppers_data.csv`) and save to `data/shopping_data_cleaned.csv`
- Perform exploratory data analysis and save plots/results to `results/`
- Build and evaluate the logistic regression model, saving confusion matrix and classification report to `results/`
- Render the Quarto report to `analysis/online-purchase-prediction.html`

To view the final report, open `analysis/online-purchase-prediction.html` in your browser.

Alternatively, render the Quarto document directly (requires Quarto installed):

```bash
quarto render analysis/online-purchase-prediction.qmd
```

### Project Structure

- `analysis/`: Quarto document and rendered HTML report
- `data/`: Raw and cleaned datasets
- `results/`: EDA plots, model confusion matrices, and classification reports
- `scripts/`: Modular Python scripts for data processing, EDA, and modeling
- `environment.yml`: Conda environment specification
- `Dockerfile`: Docker image for containerized execution
- `Makefile`: Automation script for the full pipeline

### Scripts

Individual scripts can be run separately:

- `python scripts/clean_data.py data/online_shoppers_data.csv data/shopping_data_cleaned.csv`
- `python scripts/init_eda.py data/shopping_data_cleaned.csv results/eda`
- `python scripts/create_model_and_results.py data/shopping_data_cleaned.csv results/model`

# Project Structure

```
dsci-310-group-02-team2/
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE.md
├── Makefile
├── README.md
├── analysis/
│   ├── online-purchase-prediction.html
│   ├── online-purchase-prediction.qmd
│   ├── references.bib
│   └── online-purchase-prediction_files/
│       ├── figure-html/
│       └── libs/
├── conda-lock.yml
├── environment.yml
├── data/
│   ├── online_shoppers_data.csv
│   └── shopping_data_cleaned.csv
├── results/
│   ├── eda_overview.csv
│   ├── eda_revenue_count.csv
│   └── model_classification_report.csv
└── scripts/
    ├── clean_data.py
    ├── create_model_and_results.py
    ├── init_eda.py
    └── load_data.py
```

---

# Dependencies

This project requires the following software and Python libraries:

- **Software:**
  - Docker
  - Conda or Miniconda
  - Quarto (for rendering the analysis document)

- **Python Libraries (from environment.yml):**
  - Python 3.11
  - numpy 2.3.5
  - pandas 2.3.3
  - scikit-learn 1.8.0
  - matplotlib 3.10.8
  - seaborn 0.13.2
  - jupyter 1.1.1

These dependencies will be automatically installed when building the Docker container.

---

# License

The source code for this project is licensed under the **MIT License**.

The written report and analysis are licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)** license.

Please refer to the `LICENSE.md` file for full license details.
