# Online vs In-Store Shopping Behaviour Analysis

## Contributors
- Aidan Aimy 
- Adrian Chan
- Yujia Huang
- Renata Lovette

---

# Project Summary

This project investigates whether a consumer’s level of online activity can help predict their preference for online shopping. Specifically, we examine whether factors such as internet usage, social media usage, and technological familiarity are associated with a higher likelihood of shopping online rather than in physical stores.

Using the **Online vs In-Store Shopping Behaviour dataset**, we perform exploratory data analysis and build a classification model to determine whether online activity variables can predict a consumer’s preferred shopping channel.

In addition to answering this research question, this project emphasizes **reproducible data science practices**, including version control using GitHub, literate programming using Jupyter notebooks, and containerized computational environments using Docker.

---

# Research Question

**Can consumer online activity (internet usage, social media usage, and tech-savviness) predict whether a customer prefers online shopping or in-store shopping?**

---

# Dataset

The dataset used in this project is the **Online vs In-Store Shopping Behaviour Dataset**, publicly available on Kaggle.

Dataset source:

https://www.kaggle.com/datasets/shree0910/online-vs-in-store-shopping-behaviour-dataset

The dataset contains demographic and behavioural information about consumers, including variables such as:

- Age  
- Gender  
- Income level  
- Internet usage (hours online)  
- Social media usage  
- Tech-savviness  
- Shopping frequency  
- Preferred shopping method (online vs in-store)

The target variable used in this project is **shopping channel preference**, which indicates whether a consumer prefers **online shopping or in-store shopping**.

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
   Build a classification model to predict shopping preference based on online activity and demographic features.

5. **Model Evaluation**  
   Evaluate the model's performance using appropriate metrics such as accuracy and confusion matrices.

---

# How to Run the Analysis

To reproduce this analysis, follow the steps below.

### 1. Clone the repository

```bash
git clone https://github.com/UBC-DSCI/dsci-310-group-XX-project-name.git
```

### 2. Navigate to the project directory

```bash
cd dsci-310-group-XX-project-name
```

### 3. Build the Docker image

```bash
docker build -t shopping-behaviour-analysis .
```

### 4. Run the Docker container

```bash
docker run -p 8888:8888 shopping-behaviour-analysis
```

### 5. Open the Jupyter Notebook

After launching the container, open the Jupyter link shown in the terminal and run the analysis notebook.

---

# Project Structure

```
.
├── README.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── Dockerfile
├── data/
│   └── shopping_behavior.csv
├── analysis/
│   └── shopping_activity_analysis.ipynb
└── .github/workflows/
    └── publish_docker_image.yml
```

---

# Dependencies

This project requires the following software and Python libraries:

- Python 3.10
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- Jupyter Notebook

These dependencies will be automatically installed when building the Docker container.

---

# License

The source code for this project is licensed under the **MIT License**.

The written report and analysis are licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)** license.

Please refer to the `LICENSE.md` file for full license details.
