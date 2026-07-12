from pyspark.sql import SparkSession

def get_spark_session(app_name="Chicago Crime Analysis"):
    """
    Creates or retrieves a Spark Session.
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
    return spark
