import os

# import boto3
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, \
    StringType, FloatType, TimestampType

audio_data = "/mnt/10ac-batch-5/week9/chang/kafka"
topic_input = "test"

import findspark
findspark.init('/opt/spark')

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 pyspark-shell'



def main():

    spark = SparkSession \
        .builder \
        .master('local[1]') \
        .appName("kafka-streaming-audio") \
        .getOrCreate()

    df_audio = read_from_kafka(spark)

    summarize_sales(df_audio)


def read_from_kafka(spark):#, params):
    options_read = {
        "kafka.bootstrap.servers":
            "localhost:9092",
        "subscribe":
            topic_input,
    }

    df_audio = spark.readStream \
        .format("kafka") \
        .options(**options_read) \
        .option("startingOffsets", "earliest") \
        .load()

    return df_audio


def summarize_sales(df_audio):
    schema = StructType([
        StructField("headline", StringType(), False),
        StructField("category", StringType(), False),
        StructField("article", StringType(), False),
    ])

    ds_audio = df_audio \
        .selectExpr("CAST(value AS STRING)") \
        .select(F.from_json("value", schema=schema).alias("data")) \
        .writeStream \
        .queryName("streaming_to_console") \
        .trigger(processingTime="1 minute") \
        .format("console") \
        .option("numRows", 25) \
        .option("truncate", False) \
        .start()

    ds_audio.awaitTermination()


