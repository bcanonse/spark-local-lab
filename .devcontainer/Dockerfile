FROM python:3.11-slim

# instalar java
RUN apt-get update && \
    apt-get install -y default-jdk curl && \
    apt-get clean

# instalar librerías de data engineering
RUN pip install \
    pyspark \
    pandas \
    pyarrow \
    numpy \
    ipykernel

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PYSPARK_PYTHON=python3

WORKDIR /workspace