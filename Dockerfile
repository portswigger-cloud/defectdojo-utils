FROM python:3.13-alpine

WORKDIR /usr/defectdojo-utils

COPY defectdojo ./

RUN pip install --no-cache-dir .

RUN chmod a+x src/import_scan_results.py

RUN chmod a+x src/active_findings.py

RUN chmod a+x src/findings_thresholds.py

WORKDIR /usr/defectdojo-utils/src
