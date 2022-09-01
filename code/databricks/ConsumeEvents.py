# Databricks notebook source
# DBTITLE 1,Read racing events from EventHub
connectionString = "Endpoint=sb://group2-bc-eh.servicebus.windows.net/;SharedAccessKeyName=dbr;SharedAccessKey=h7I9AXXw6PDUltFf8TUZMIBjjaBAUTRq4ltwJqjhl/0=;EntityPath=group2-demo-eh"

ehConf = {}
ehConf['eventhubs.connectionString'] = sc._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt(connectionString)
ehConf['eventhubs.consumerGroup'] = "dbr"


df = spark.readStream.format("eventhubs").options(**ehConf).load()
display(df)

# COMMAND ----------

# DBTITLE 1,Decode EventHub data in DataFrame
# Write stream into defined sink

from pyspark.sql.types import *

import  pyspark.sql.functions as F

events_schema = StructType([
  StructField("boat", StringType(), True),
  StructField("latitude", DoubleType(), True),
  StructField("longitude", DoubleType(), True),
  StructField("heading", DoubleType(), True),
  StructField("speed", DoubleType(), True)])

decoded_df = df.select(F.from_json(F.col("body").cast("string"), events_schema).alias("Payload"), F.col('enqueuedTime'),F.col('partition'), F.col('sequenceNumber'))

df_events = decoded_df.select(decoded_df.Payload.boat.alias('boat'), decoded_df.Payload.latitude.alias('latitude'), decoded_df.Payload.longitude.alias('longitude'), decoded_df.Payload.heading.alias('heading'), decoded_df.Payload.speed.alias('speed'),decoded_df.enqueuedTime.alias('enqueuedTime'),decoded_df.partition.alias('partition'),decoded_df.sequenceNumber.alias('sequenceNumber'))


display(df_events)


# COMMAND ----------

# DBTITLE 1,Filter garbled datastream and write to Raw Delta table
df_events.filter((df_events.latitude > -90) & (df_events.latitude < 90))\
  .writeStream\
  .format("delta")\
  .outputMode("append")\
  .option("checkpointLocation", "delta/events/checkpoints/raw/boating")\
  .toTable("raw_boating")
