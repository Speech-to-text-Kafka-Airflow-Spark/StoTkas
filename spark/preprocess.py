import os
import boto3

dataset_path = '/home/samuel_alene/data'

# Subscribe to 1 topic, with headers
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1") \
  .option("includeHeaders", "true") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)", "headers")

def upload_file(file_name: str, bucket: str, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    
    response = s3_client.upload_file(file_name, bucket, object_name)
    
    return True