# Databricks notebook source
# DBTITLE 1,Create Raw and Aggregate Tables
# MAGIC %sql
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE raw_boating (
# MAGIC boat STRING, 
# MAGIC latitude DOUBLE, 
# MAGIC longitude DOUBLE,
# MAGIC heading DOUBLE,
# MAGIC speed  DOUBLE,
# MAGIC enqueuedTime timestamp,
# MAGIC partition string,
# MAGIC sequenceNumber long
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE agg_boating (
# MAGIC boat string,
# MAGIC lat1 double,
# MAGIC lon1 double,
# MAGIC lat2 double,
# MAGIC lon2 double,
# MAGIC timer timestamp,
# MAGIC distanceTravelled double
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC insert into agg_boating select * from agg_boating_2

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from agg_boating

# COMMAND ----------


