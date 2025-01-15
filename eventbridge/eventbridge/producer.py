import json
import logging
from typing import List, Dict, Any

from confluent_kafka import Producer, KafkaError, Message
from confluent_kafka.admin import AdminClient, NewTopic

from eventbridge.datalake import RawEvent

_CONFIG = {"bootstrap.servers": "kafka:9092,localhost:29092"}


def create_topic(topic_name: str) -> None:
    admin_client = AdminClient(_CONFIG)

    new_topic = NewTopic(topic_name, num_partitions=3, replication_factor=1)
    create_topics_result = admin_client.create_topics([new_topic])
    for topic, response in create_topics_result.items():
        try:
            response.result()
            logging.info("Topic %s created", topic)
        except KafkaError as error:
            logging.error("Failed to create topic %s: %s", topic, error)


def delivery_report(error: KafkaError, message: Message) -> None:
    if error is not None:
        logging.info("Message delivery failed: %s", error)
    else:
        logging.info(
            "Message delivered to %s [%s]", message.topic(), message.partition()
        )


def publish_raw_events(
    config: Dict[str, Any], topic: str, raw_events: List[RawEvent]
) -> None:
    producer = Producer(config)
    for raw_event in raw_events:
        producer.poll(0)
        producer.produce(
            topic, json.dumps(raw_event).encode("utf-8"), callback=delivery_report
        )
    producer.flush()
