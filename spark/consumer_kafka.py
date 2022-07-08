import os

# import boto3
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, \
    StringType, FloatType, TimestampType

sales_data = "../data/clean_data.csv"
topic_input = "pagila.sales.spark.streaming"

import findspark
findspark.init('/opt/spark')

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 pyspark-shell'



def main():

    spark = SparkSession \
        .builder \
        .appName("kafka-streaming-sales-console") \
        .getOrCreate()

    df_sales = read_from_kafka(spark)#, params)

    summarize_sales(df_sales)


def read_from_kafka(spark):#, params):
    options_read = {
        "kafka.bootstrap.servers":
            "localhost:9092",
        "subscribe":
            topic_input,
    }

    df_sales = spark.readStream \
        .format("kafka") \
        .options(**options_read) \
        .load()

    return df_sales


def summarize_sales(df_sales):
    schema = StructType([
        StructField("headline", StringType(), False),
        StructField("category", StringType(), False),
        StructField("article", StringType(), False),
    ])

    ds_sales = df_sales \
        .selectExpr("CAST(value AS STRING)") \
        .select(F.from_json("value", schema=schema).alias("data")) \
        .writeStream \
        .queryName("streaming_to_console") \
        .trigger(processingTime="1 minute") \
        .format("console") \
        .option("numRows", 25) \
        .option("truncate", False) \
        .start()

    ds_sales.awaitTermination()





if __name__ == "__main__":
    main()