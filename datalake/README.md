# Datalake
Holds the analytical data necessary to create price estimations.

The original dataset is taken from: https://www.kaggle.com/olistbr/brazilian-ecommerce/?select=olist_order_items_dataset.csv

The folders are:
* events (should contain events in `.parquet` format)
* jobs (should contain packaged jobs that can be executed with a job scheduler)
* prices (domain folder that contains all data related to the domain prices)
* raw (contains the raw source data)

## events
Contains the results of the eventbridge. The events should be ordered by `topic`/`year`/`month`/`day`/`hour`/`timestamp`.parquet.
The finest granularity to get events is by the hour.
