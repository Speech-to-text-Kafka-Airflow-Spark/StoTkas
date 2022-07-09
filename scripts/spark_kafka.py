import os
import boto3

import findspark
findspark.init('/opt/spark')

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 pyspark-shell'


from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .master('local[1]') \
                    .appName('audio') \
                    .getOrCreate()




# df.printSchema()

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "test") \
    .option("startingOffsets", "earliest") \
    .load()



query = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .format("console") \
    .option("checkpointLocation", "/mnt/10ac-batch-5/week9/chang/kafka") \
    .start()


query.awaitTermination()