FROM python:3.10
#RUN apt update && apt install -y librdkafka-dev python-dev && apt autoclean
RUN apt update && apt install -y librdkafka-dev python-dev-is-python3 && apt autoclean
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY eventbridge ./eventbridge
ENV PYTHONPATH=/usr/src/app

RUN useradd -M -s /bin/bash eventbridge && chown -R eventbridge:eventbridge /usr/src/app
USER eventbridge
RUN ls -all
CMD [ "python", "eventbridge/main.py", "--raw-events-file", "/datalake/raw/0001/olist_order_items_dataset.csv" ]
