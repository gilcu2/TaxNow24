FROM python:3.10-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY jobs ./jobs
ENV PYTHONPATH=/usr/src/app

RUN useradd -M -s /bin/bash jobs && chown -R jobs:jobs /usr/src/app
USER jobs

CMD [ "python", "jobs/main.py" ]
