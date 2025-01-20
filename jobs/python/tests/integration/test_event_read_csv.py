from datetime import datetime

from jobs.event_read_csv import read_event_csv
from tests import SPARK
from chispa.dataframe_comparer import assert_df_equality


def test_read_orders():
    filename = "tests/integration/fixtures/dataset.csv"
    actual = read_event_csv(SPARK, filename)

    expected = SPARK.createDataFrame(
        [
            [
                "00010242fe8c5a6d1ba2dd792cb16214",
                1,
                "4244733e06e7ecb4970a6e2683c13e61",
                "48436dade18ac8b2bce089ec2a041202",
                datetime(2017, 9, 19, 9, 45, 35),
                58.90,
                13.29,
            ],
            [
                "00018f77f2f0320c557190d7a144bdd3",
                1,
                "e5f2d52b802189ee658865ca93d83a8f",
                "dd7ddc04e1b6c2c614352b383efe2d36",
                datetime(2017, 5, 3, 11, 5, 13),
                239.90,
                19.93,
            ],
            [
                "00024acbcdf0a6daa1e931b038114c75",
                1,
                "7634da152a4610f1595efa32f14722fc",
                "9d7a1d34a5052409006425275ba1c2b4",
                datetime(2018, 8, 15, 10, 10, 18),
                12.99,
                12.79,
            ],
            [
                "0005a1a1728c9d785b8e2b08b904576c",
                1,
                "310ae3c140ff94b03219ad0adc3c778f",
                "a416b6a846a11724393025641d4edd5e",
                datetime(2018, 3, 26, 18, 31, 29),
                145.95001,
                11.65,
            ],
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

    assert_df_equality(actual, expected)
