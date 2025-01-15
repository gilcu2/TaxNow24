from pyspark.sql import DataFrame, SparkSession


def aggregate_users_by_usage(spark: SparkSession, dataframe: DataFrame) -> DataFrame:
    return dataframe


def run(spark: SparkSession, input_path: str, output_path: str) -> None:
    input_dataset = spark.read.parquet(input_path)
    input_dataset.show()

    aggregated_users = aggregate_users_by_usage(spark, input_dataset)
    aggregated_users.show()

    aggregated_users.write.parquet(output_path, mode="append")
