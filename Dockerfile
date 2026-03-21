FROM continuumio/miniconda3:23.10.0-1

WORKDIR /app

# 1. Install system dependencies needed for Quarto and Chromium
RUN apt-get update && apt-get install -y \
    curl \
    gconf-service \
    libasound2 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgbm1 \
    libgcc1 \
    libgconf-2-4 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libstdc++6 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    lsb-release \
    xdg-utils \
    wget \
    && rm -rf /var/lib/apt/lists/*

# 2. Install Quarto (specifically the version for Linux AMD64)
RUN curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.550/quarto-1.4.550-linux-arm64.deb \
  && dpkg -i quarto-1.4.550-linux-arm64.deb \
  && rm quarto-1.4.550-linux-arm64.deb

# 3. Create the Conda environment (Make sure to remove 'quarto' from your environment.yml first!)
COPY environment.yml .
RUN conda env create -f environment.yml && conda clean -afy

COPY . .

# Use conda run to execute the notebook
CMD ["conda", "run", "--no-capture-output", "-n", "dsci-310-team2", \
     "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", \
     "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]