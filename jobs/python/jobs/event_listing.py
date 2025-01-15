from pyspark.sql import DataFrame, SparkSession


def list_events(spark: SparkSession, dataframe: DataFrame) -> DataFrame:
    return dataframe


def run(spark: SparkSession, input_path: str, output_path: str) -> None:
    input_dataset = spark.read.csv(input_path)
    input_dataset.show()

    partitioned_events = list_events(spark, input_dataset)
    partitioned_events.show()

    partitioned_events.write.format("avro").save(output_path, mode="append")
