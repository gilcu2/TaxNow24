from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, StringType
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


def partition_events(spark: SparkSession, dataframe: DataFrame) -> DataFrame:
    with_partitions_columns = (
        dataframe.withColumn("year", year("shipping_limit_date").cast(LongType()))
        .withColumn("month", month("shipping_limit_date").cast(LongType()))
        .withColumn("day", dayofmonth("shipping_limit_date").cast(LongType()))
        .withColumn("hour", hour("shipping_limit_date").cast(LongType()))
        .withColumn("minute", minute("shipping_limit_date").cast(LongType()))
        .withColumn("second", second("shipping_limit_date").cast(LongType()))
    )
    return with_partitions_columns


def run(spark: SparkSession, input_path: str, output_path: str) -> None:
    input_dataset = spark.read.csv(input_path)
    input_dataset.show()

    partitioned_events = partition_events(spark, input_dataset)
    partitioned_events.show()

    partitioned_events.write.format("avro").save(output_path, mode="append")
