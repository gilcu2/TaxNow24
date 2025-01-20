from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import (
    year,
    month,
    dayofmonth,
    hour,
    minute,
    second,
    to_timestamp,
    when,
    col,
    from_unixtime,
)
from pyspark.sql.types import (
    StructField,
    StructType,
    TimestampType,
    StringType,
    IntegerType,
    DoubleType,
    LongType,
)


def read_order_csv(spark: SparkSession, filename: str) -> DataFrame:
    schema = StructType(
        [
            StructField("order_id", StringType()),
            StructField("order_item_id", LongType()),
            StructField("product_id", StringType()),
            StructField("seller_id", StringType()),
            StructField("shipping_limit_date", StringType()),
            StructField("price", DoubleType()),
            StructField("freight_value", DoubleType()),
        ]
    )

    df = (
        spark.read.schema(schema)
        .options(header=True, enableDateTimeParsingFallback=True)
        .csv(filename)
    )
    without_null = df.filter(df.product_id.isNotNull())

    with_date_time = without_null.withColumn(
        "shipping_limit_date",
        when(
            col("shipping_limit_date").contains(":"),
            to_timestamp("shipping_limit_date"),
        )
        .otherwise(from_unixtime("shipping_limit_date"))
        .cast(TimestampType()),
    )

    return with_date_time
