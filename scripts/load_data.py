import os
import boto3
import pandas as pd


DATASET_PATH = "/mnt/10ac-batch-5/week9/chang/kafka"
def load_data_s3(bucket_name=DATASET_PATH, file_name='Clean_Amharic.txt'):
    """ Load transcription data from s3 bucket"""
    
    # Load file directly into python
    obj = bucket_name.Object(file_name).get()
    df = pd.read_csv(obj['Body'])
    return df