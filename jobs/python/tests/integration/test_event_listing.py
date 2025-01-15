from jobs.event_listing import list_events
from tests import SPARK


def test_should_list_events():
    test_data = SPARK.read.csv("tests/integration/fixtures/simple_dataset.csv")

    actual = list_events(SPARK, test_data)
    expected = SPARK.createDataFrame(
        [
            [
                "00000000000000000000000000000000",
                "11",
                "22222222222222222222222222222222",
                "33333333333333333333333333333333",
                "2004-04-04 04:44:44",
                "55.55",
                "66.66",
            ],
        ],
    )

    assert expected.collect() == actual.collect()
