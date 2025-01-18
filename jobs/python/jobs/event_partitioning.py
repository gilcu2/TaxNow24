from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import year, month, dayofmonth,hour,minute,second


def partition_events(spark: SparkSession, dataframe: DataFrame) -> DataFrame:
    without_null=dataframe.filter(dataframe.product_id.isNotNull())
    with_columns=(without_null
                  .withColumn("year",year(without_null.shipping_limit_date))
                  .withColumn("month", month(without_null.shipping_limit_date))
                  .withColumn("day", dayofmonth(without_null.shipping_limit_date))
                  .withColumn("hour", hour(without_null.shipping_limit_date))
                  .withColumn("minute", minute(without_null.shipping_limit_date))
                  .withColumn("second", second(without_null.shipping_limit_date))
                  )
    return with_columns


def run(spark: SparkSession, input_path: str, output_path: str) -> None:
    input_dataset = spark.read.csv(input_path)
    input_dataset.show()

    partitioned_events = partition_events(spark, input_dataset)
    partitioned_events.show()

    partitioned_events.write.format("avro").save(output_path, mode="append")
