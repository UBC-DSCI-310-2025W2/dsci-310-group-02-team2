FROM continuumio/miniconda3

WORKDIR /app
COPY environment.yml .
RUN conda env create -f environment.yml && conda clean -afy
COPY . .
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
CMD ["python", "main.py"]