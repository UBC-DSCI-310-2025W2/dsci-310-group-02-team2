FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml && conda clean -afy

COPY . .

CMD ["conda", "run", "--no-capture-output", "-n", "dsci-310-team2", "python", "-c", "import numpy, pandas, sklearn, matplotlib; print('environment works')"]