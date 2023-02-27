FROM python:3.11-alpine

WORKDIR /usr/defectdojo-utils

COPY defectdojo ./

RUN pip install --no-cache-dir .

RUN chmod a+x src/import_scan_results.py

RUN chmod a+x src/active_findings.py

WORKDIR /usr/defectdojo-utils/src