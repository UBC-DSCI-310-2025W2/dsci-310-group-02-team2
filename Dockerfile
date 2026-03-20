FROM continuumio/miniconda3:23.10.0-1

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml && conda clean -afy

COPY . .

CMD ["conda", "run", "--no-capture-output", "-n", "dsci-310-team2", \
     "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", \
     "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]