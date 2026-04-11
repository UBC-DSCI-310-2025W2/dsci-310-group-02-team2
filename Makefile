# Makefile
# usage: make all --> generate final report
# Group 2, DSCI 310
# Automates full analysis pipeline within Docker

# --- Variables ---
IMAGE_NAME = quarto-env
DOCKER_RUN = docker run --rm -v "$(shell pwd):/app" -w /app $(IMAGE_NAME)
CONDA_EXEC = conda run --no-capture-output -n dsci-310-team2

# --- .PHONY Targets ---
.PHONY: all clean data_processing eda modeling report

# --- Main Target ---
all: report

# --- 1. Data Processing ---
data_processing: data/shopping_data_cleaned.csv

data/shopping_data_cleaned.csv: data/online_shoppers_data.csv scripts/clean_data.py
	$(DOCKER_RUN) $(CONDA_EXEC) bash -c "PYTHONPATH=. python scripts/clean_data.py \
		data/online_shoppers_data.csv \
		data/shopping_data_cleaned.csv"

# --- 2. Exploratory Data Analysis (EDA) ---
eda: results/eda_correlation_heatmap.png

results/eda_correlation_heatmap.png: data/shopping_data_cleaned.csv scripts/init_eda.py
	$(DOCKER_RUN) $(CONDA_EXEC) bash -c "PYTHONPATH=. python scripts/init_eda.py \
		data/shopping_data_cleaned.csv \
		results/eda"

# --- 3. Modeling ---
modeling: results/model_confusion_matrix.png

results/model_confusion_matrix.png: data/shopping_data_cleaned.csv scripts/create_model_and_results.py
	$(DOCKER_RUN) $(CONDA_EXEC) bash -c "PYTHONPATH=. python scripts/create_model_and_results.py \
		data/shopping_data_cleaned.csv \
		results/model"

# --- 4. Final Report ---
report: online-purchase-prediction.html

online-purchase-prediction.html: analysis/online-purchase-prediction.qmd eda modeling
	$(DOCKER_RUN) $(CONDA_EXEC) quarto render analysis/online-purchase-prediction.qmd \
		--to html \
		--output-dir .

# --- 5. Cleaning ---
clean:
	rm -f data/shopping_data_cleaned.csv
	rm -f results/*
	rm -f online-purchase-prediction.html
	rm -rf analysis/online-purchase-prediction_files