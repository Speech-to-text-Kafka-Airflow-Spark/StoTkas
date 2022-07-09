import os

import boto3
import pyspark.sql.functions as F
# from ec2_metadata import ec2_metadata
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, \
    StringType, FloatType
from pyspark.sql.window import Window

sales_data = "/home/sam/Desktop/10_acad/week_9/streaming_app/data/clean_data.csv"
topic_output = "test"

import findspark
findspark.init('/opt/spark')

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 pyspark-shell'

# ssm_client = boto3.client("ssm")


def main():
    # params = get_parameters()

    spark = SparkSession \
        .builder \
        .master('local[1]') \
        .appName("kafka-spark") \
        .getOrCreate()

    df_sales = read_from_csv(spark)#, params)

    write_to_kafka(df_sales)


def read_from_csv(spark):    #, params):
    schema = StructType([
        StructField("headline", StringType(), False),
        StructField("category", StringType(), False),
        StructField("article", StringType(), False),
    ])

    df_sales = spark.read \
        .csv(path=sales_data, #f"s3a://{params['kafka_demo_bucket']}/spark/{sales_data}",
             schema=schema, header=True, sep="|")

    # optional
    # df_sales = update_payment_date(df_sales)

    return df_sales


def write_to_kafka(df_sales):
    options_write = {
        "kafka.bootstrap.servers":
            "localhost:9092",
        "topic":
            topic_output,
        # "kafka.ssl.truststore.location":
        #     "/tmp/kafka.client.truststore.jks",
        # "kafka.security.protocol":
        #     "SASL_SSL",
        # "kafka.sasl.mechanism":
        #     "AWS_MSK_IAM",
        # "kafka.sasl.jaas.config":
        #     "software.amazon.msk.auth.iam.IAMLoginModule required;",
        # "kafka.sasl.client.callback.handler.class":
        #     "software.amazon.msk.auth.iam.IAMClientCallbackHandler",
    }
    # .format("console") \
    df_sales \
        .selectExpr("CAST(headline AS STRING) AS key",
                    "to_json(struct(*)) AS value") \
        .write \
        .format("console") \
        .option("checkpointLocation", "/home/sam/Desktop/10_acad/week_9/streaming_app/data/kafka")  \
        .save()


# def update_payment_date(df):
#     """Update existing payment date to a current timestamp for streaming simulation"""

#     record_count = 250
#     window = Window.orderBy("payment_id")
#     df = df \
#         .drop("payment_date") \
#         .withColumn("index", F.row_number().over(window)) \
#         .withColumn("payment_date",
#                     (F.unix_timestamp(F.current_timestamp()) -
#                      (record_count - F.col("index"))).cast(IntegerType())) \
#         .drop("index")

#     return df


# def get_parameters():
#     """Load parameter values from AWS Systems Manager (SSM) Parameter Store"""

#     params = {
#         "kafka_servers": ssm_client.get_parameter(
#             Name="/kafka_spark_demo/kafka_servers")["Parameter"]["Value"],
#         "kafka_demo_bucket": ssm_client.get_parameter(
#             Name="/kafka_spark_demo/kafka_demo_bucket")["Parameter"]["Value"],
#     }

#     return params


if __name__ == "__main__":
    main()
