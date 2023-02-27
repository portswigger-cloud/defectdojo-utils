FROM python:3.11-alpine

WORKDIR /usr/defectdojo-utils

COPY defectdojo ./

RUN pip install --no-cache-dir .

WORKDIR /usr/defectdojo-utils/src