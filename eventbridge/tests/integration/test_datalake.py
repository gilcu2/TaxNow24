from eventbridge.datalake import load_raw_data


def test_should_load_raw_csv_content():
    path = "tests/integration/resources/raw.csv"

    actual = load_raw_data(path)
    expected = [
        {
            "freight_value": 13.29,
            "order_id": "00010242fe8c5a6d1ba2dd792cb16214",
            "order_item_id": 1,
            "price": 58.9,
            "product_id": "4244733e06e7ecb4970a6e2683c13e61",
            "seller_id": "48436dade18ac8b2bce089ec2a041202",
            "shipping_limit_date": "2017-09-19 09:45:35",
        },
        {
            "freight_value": 19.93,
            "order_id": "00018f77f2f0320c557190d7a144bdd3",
            "order_item_id": 1,
            "price": 239.9,
            "product_id": "e5f2d52b802189ee658865ca93d83a8f",
            "seller_id": "dd7ddc04e1b6c2c614352b383efe2d36",
            "shipping_limit_date": "2017-05-03 11:05:13",
        },
        {
            "freight_value": 17.87,
            "order_id": "000229ec398224ef6ca0657da4fc703e",
            "order_item_id": 1,
            "price": 199.0,
            "product_id": "c777355d18b72b67abbeef9df44fd0fd",
            "seller_id": "5b51032eddd242adc84c38acab88f23d",
            "shipping_limit_date": "2018-01-18 14:48:30",
        },
    ]

    assert expected == actual
