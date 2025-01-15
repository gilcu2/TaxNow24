from jobs.event_partitioning import partition_events
from tests import SPARK


def test_should_return_one_event_with_date_transformed():
    dataframe = SPARK.createDataFrame(
        [
            [
                "1337",
                42,
                "1337-42",
                "foobar1337",
                "2017-09-19 09:45:35",
                42.0,
                13.37,
            ]
        ],
        [
            "order_id",
            "order_item_id",
            "product_id",
            "seller_id",
            "shipping_limit_date",
            "price",
            "freight_value",
        ],
    )

    actual = partition_events(SPARK, dataframe)
    expected = SPARK.createDataFrame(
        [
            [
                "1337",
                42,
                "1337-42",
                "foobar1337",
                "2017-09-19 09:45:35",
                42.0,
                13.37,
                2017,
                9,
                19,
                9,
                45,
                35,
            ]
        ],
        [
            "order_id",
            "order_item_id",
            "product_id",
            "seller_id",
            "shipping_limit_date",
            "price",
            "freight_value",
            "year",
            "month",
            "day",
            "hour",
            "minute",
            "second",
        ],
    )

    assert expected.collect() == actual.collect()
