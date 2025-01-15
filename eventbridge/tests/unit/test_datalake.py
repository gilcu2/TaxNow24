from eventbridge.datalake import transform_raw_event


def test_should_return_one_raw_event():
    raw_event = (
        '"00010242fe8c5a6d1ba2dd792cb16214",'
        "1,"
        '"4244733e06e7ecb4970a6e2683c13e61",'
        '"48436dade18ac8b2bce089ec2a041202",'
        "2017-09-19 09:45:35,"
        "58.90,"
        "13.29"
    )

    actual = transform_raw_event(raw_event)
    expected = {
        "order_id": "00010242fe8c5a6d1ba2dd792cb16214",
        "order_item_id": 1,
        "product_id": "4244733e06e7ecb4970a6e2683c13e61",
        "seller_id": "48436dade18ac8b2bce089ec2a041202",
        "shipping_limit_date": "2017-09-19 09:45:35",
        "price": 58.90,
        "freight_value": 13.29,
    }

    assert expected == actual


def test_should_return_another_raw_event():
    raw_event = '"foobar",2,"foo","bar",2018-11-01 12:13:37,42.00,13.37'

    actual = transform_raw_event(raw_event)
    expected = {
        "order_id": "foobar",
        "order_item_id": 2,
        "product_id": "foo",
        "seller_id": "bar",
        "shipping_limit_date": "2018-11-01 12:13:37",
        "price": 42.0,
        "freight_value": 13.37,
    }

    assert expected == actual
