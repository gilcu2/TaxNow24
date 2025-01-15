import json
import logging
from typing import Any, Dict

from confluent_kafka import Consumer

from eventbridge.datalake import persist_raw_event


def persist_events(config: Dict[str, Any], topic: str) -> None:
    consumer = Consumer(
        {"group.id": "price_estimation", "auto.offset.reset": "earliest", **config}
    )

    consumer.subscribe([topic])

    while True:
        message = consumer.poll(1.0)

        if message is None:
            continue
        if message.error():
            logging.error("Consumer error: %s", message.error())
            continue

        message_value = message.value()
        logging.info("Received message: %s", message_value)
        raw_event = json.loads(message_value)
        persist_raw_event(raw_event)

    consumer.close()
