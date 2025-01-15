import logging

from jobs import event_partitioning
from jobs.spark_settings import setup_spark

APP_NAME = "EVENT_PARTITIONING"

if __name__ == "__main__":
    input_path, output_path, spark = setup_spark(APP_NAME)
    event_partitioning.run(spark, input_path, output_path)
    logging.info("Application Done: %s", spark.sparkContext.appName)
    spark.stop()
