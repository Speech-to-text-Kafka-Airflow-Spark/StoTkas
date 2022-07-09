import findspark
findspark.init('/opt/spark')

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 pyspark-shell'

import time
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sec = 1
topic = "quickstart-events"

conf = SparkConf().setAppName.appName('SparkByExamples.com').setMaster('local[*]')
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, sec)

kafkaStream = KafkaUtils.createDirectStream(ssc, [topic],{
    "kafka.bootstrap.servers": "localhost:9092",
    "group.id" : "video-group",
    "fetch.message.max_bytes": "15728648",
    "auto.offset.reset":'largest'})

# lines = kvs.map(lambda x: x[1])

ssc.start()
time.sleep(600)
ssc.stop(stopSparkContext=True, stopGracefully=True)

