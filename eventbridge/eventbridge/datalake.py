import logging
import os
from os.path import exists
from datetime import datetime
from typing import TypedDict, List

import pandas as pd

BASE_PATH = "/datalake"


class RawEvent(TypedDict):
    order_id: str
    order_item_id: int
    product_id: str
    seller_id: str
    shipping_limit_date: str
    price: float
    freight_value: float


def transform_raw_event(raw_event: str) -> RawEvent:
    columns = raw_event.split(",")
    return {
        "order_id": columns[0].replace('"', ""),
        "order_item_id": int(columns[1]),
        "product_id": columns[2].replace('"', ""),
        "seller_id": columns[3].replace('"', ""),
        "shipping_limit_date": columns[4],
        "price": float(columns[5]),
        "freight_value": float(columns[6]),
    }


def load_raw_data(path: str) -> List[RawEvent]:
    with open(path, "r", encoding="UTF-8") as raw_events_file:
        lines = raw_events_file.readlines()
        return list(map(transform_raw_event, lines[1:]))


def persist_raw_event(raw_event: RawEvent) -> None:
    event_time = datetime.strptime(
        raw_event["shipping_limit_date"], "%Y-%m-%d %H:%M:%S"
    )
    path = (
        f"{BASE_PATH}/events/pricing_events/"
        f"{event_time.strftime('%Y')}/{event_time.strftime('%m')}/"
        f"{event_time.strftime('%d')}/{event_time.strftime('%H')}"
    )
    data_frame = pd.DataFrame([raw_event])
    try:
        os.makedirs(path)
    except FileExistsError:
        logging.info("folder already exists for %s", path)
    parquet_file_name = f"{path}/{event_time.timestamp()}.parquet"
    if not exists(parquet_file_name):
        data_frame.to_parquet(parquet_file_name)
