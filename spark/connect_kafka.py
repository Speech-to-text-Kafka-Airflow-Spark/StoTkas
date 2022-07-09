import os
import boto3

import findspark
findspark.init('/opt/spark')

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 pyspark-shell'


from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .master('local[1]') \
                    .appName('SparkByExamples.com') \
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
    .option("checkpointLocation", "/home/sam/Desktop/10_acad/week_9/streaming_app/data/kafka") \
    .start()


query.awaitTermination()

df.printSchema()

# def upload_file(file_name: str, bucket: str, object_name=None):
#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = os.path.basename(file_name)

#     # Upload the file
#     s3_client = boto3.client('s3')
    
#     response = s3_client.upload_file(file_name, bucket, object_name)
    
#     return True