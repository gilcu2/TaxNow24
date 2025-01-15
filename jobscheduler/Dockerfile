FROM python:3.10
#ENV DEBIAN_FRONTEND noninteractive
#RUN apt-get update && apt-get install -y setproctitle
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY jobscheduler ./jobscheduler
ENV PYTHONPATH=/usr/src/app
ENV AIRFLOW_HOME=/usr/src/app/jobscheduler
RUN useradd -M -s /bin/bash jobscheduler && chown -R jobscheduler:jobscheduler /usr/src/app
USER jobscheduler

CMD [ "airflow", "standalone" ]
