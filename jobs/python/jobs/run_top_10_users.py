import logging

from jobs import user_aggregation
from jobs.spark_settings import setup_spark

APP_NAME = "TOP_10_DASHBOARD"

if __name__ == "__main__":
    input_path, output_path, spark = setup_spark(APP_NAME)
    user_aggregation.run(spark, input_path, output_path)
    logging.info("Application Done: %s", spark.sparkContext.appName)
    spark.stop()
