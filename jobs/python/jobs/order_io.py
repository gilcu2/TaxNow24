from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import year, month, dayofmonth, hour, minute, second


def read_order_csv(spark: SparkSession, filename: str) -> DataFrame:
    df = spark.read.csv(filename, header=True, inferSchema=False)
    without_null = df.filter(df.product_id.isNotNull())
    with_columns = (without_null
                    .withColumn("year", year(without_null.shipping_limit_date))
                    .withColumn("month", month(without_null.shipping_limit_date))
                    .withColumn("day", dayofmonth(without_null.shipping_limit_date))
                    .withColumn("hour", hour(without_null.shipping_limit_date))
                    .withColumn("minute", minute(without_null.shipping_limit_date))
                    .withColumn("second", second(without_null.shipping_limit_date))
                    )
    return with_columns
