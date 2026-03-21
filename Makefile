# Makefile
# usgae: make all --> open online-purchase-prediction.html in browser to view the final report.
# Group 2, DSCI 310
# This driver script automates the entire analysis pipeline within Docker.

# --- Variables ---
IMAGE_NAME = quarto-env
# Using $(shell pwd) or $(CURDIR) to mount the local directory to /app in the container
DOCKER_RUN = docker run --rm -v "$(shell pwd):/app" $(IMAGE_NAME)
CONDA_EXEC = conda run --no-capture-output -n dsci-310-team2

# --- .PHONY Targets ---
.PHONY: all clean data_processing eda modeling report

# --- Main Target ---
# Running 'make all' will check every step of the pipeline
all: report

# --- 1. Data Processing ---
# Cleans raw data and produces the cleaned CSV
data_processing: data/shopping_data_cleaned.csv

data/shopping_data_cleaned.csv: data/online_shoppers_data.csv scripts/clean_data.py
	$(DOCKER_RUN) $(CONDA_EXEC) python scripts/clean_data.py \
		data/online_shoppers_data.csv \
		data/shopping_data_cleaned.csv

# --- 2. Exploratory Data Analysis (EDA) ---
# Depends on cleaned data; generates plots in results/
eda: results/eda_correlation_heatmap.png

results/eda_correlation_heatmap.png: data/shopping_data_cleaned.csv scripts/init_eda.py
	$(DOCKER_RUN) $(CONDA_EXEC) python scripts/init_eda.py \
		data/shopping_data_cleaned.csv \
		results/eda

# --- 3. Modeling ---
# Depends on cleaned data; generates results/plots
modeling: results/model_confusion_matrix.png

results/model_confusion_matrix.png: data/shopping_data_cleaned.csv scripts/create_model_and_results.py
	$(DOCKER_RUN) $(CONDA_EXEC) python scripts/create_model_and_results.py \
		data/shopping_data_cleaned.csv \
		results/model

# --- 4. Final Report (The .qmd Render) ---
# Depends on the .qmd file AND the output of the EDA and Modeling steps
report: online-purchase-prediction.html

online-purchase-prediction.html: analysis/online-purchase-prediction.qmd eda modeling
	$(DOCKER_RUN) $(CONDA_EXEC) quarto render analysis/online-purchase-prediction.qmd \
		--to html \
		--output-dir ..

# --- 5. Cleaning ---
# Deletes all generated files to reset the project state
clean:
	rm -f data/shopping_data_cleaned.csv
	rm -f results/*
	rm -f online-purchase-prediction.html
	rm -rf analysis/online-purchase-prediction_files


