 # Makefile
# Group 2, DSCI 310
# This driver script automates the analysis pipeline within Docker.

# Variables for consistency
IMAGE_NAME = quarto-env
DOCKER_RUN = docker run --rm -v "$(CURDIR):/app" $(IMAGE_NAME)
CONDA_EXEC = conda run --no-capture-output -n dsci-310-team2

.PHONY: all data analysis figures clean-all

# --- Main Target ---
all: report.html

# --- 1. Data (Static) ---
# We no longer "build" this file; we just acknowledge it exists.
data/online_shoppers_data.csv:
	@echo "Data file already exists in data/ folder."

# --- 2. Data Processing ---
# This now depends ONLY on the file being there and the script.
data/shopping_data_cleaned.csv: data/online_shoppers_data.csv scripts/clean_data.py
	$(DOCKER_RUN) $(CONDA_EXEC) python scripts/clean_data.py \
		data/online_shoppers_data.csv \
		data/shopping_data_cleaned.csv
		

# --- 3. Exploratory Analysis ---
# Generates EDA plots and tables
analysis: results/eda_correlation_heatmap.png

results/eda_correlation_heatmap.png: data/shopping_data_cleaned.csv scripts/init_eda.py
	$(DOCKER_RUN) $(CONDA_EXEC) python scripts/init_eda.py \
		data/shopping_data_cleaned.csv \
		results/eda

# --- 4. Modeling ---
# Generates model results
figures: results/model_confusion_matrix.png

results/model_confusion_matrix.png: data/shopping_data_cleaned.csv scripts/create_model_and_results.py
	$(DOCKER_RUN) $(CONDA_EXEC) python scripts/create_model_and_results.py \
		data/shopping_data_cleaned.csv \
		results/model

# --- 5. Final Report ---
# Renders the Quarto report
report.html: analysis/online-purchase-prediction.ipynb analysis figures
	$(DOCKER_RUN) $(CONDA_EXEC) quarto render analysis/online-purchase-prediction.ipynb --to html --output-dir .

# --- Cleaning ---
clean-all:
	rm -f data/shopping_data_cleaned.csv
	rm -f results/*
	rm -f online-purchase-prediction.html