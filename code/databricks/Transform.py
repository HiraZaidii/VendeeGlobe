# Databricks notebook source
# DBTITLE 1,Aggregate Raw Data Hourly
df = spark.sql('''
with cte as(
select
  boat
  ,latitude
  ,longitude
  ,enqueuedTime
  ,date_format(enqueuedTime,'yyyyMMddHH') as Timer 
from raw_boating_2
)
select distinct
  boat
  ,FIRST_VALUE(latitude) OVER (PARTITION BY boat,Timer ORDER BY enqueuedTime) AS lat1
  ,FIRST_VALUE(longitude) OVER (PARTITION BY boat,Timer ORDER BY enqueuedTime) AS lon1
  ,FIRST_VALUE(latitude) OVER (PARTITION BY boat,Timer ORDER BY enqueuedTime desc) AS lat2
  ,FIRST_VALUE(longitude) OVER (PARTITION BY boat,Timer ORDER BY enqueuedTime desc) AS lon2
  ,to_timestamp(Timer,'yyyyMMddHH') AS Timer 
from cte
order by boat,timer
''')

df.show()


# COMMAND ----------

# DBTITLE 1,Calculate Distance Travelled using Python Geopy.geodesic module
from geopy.distance import geodesic
import pyspark.sql.functions as F

@F.udf()
def geodesic_udf(a, b):
    return geodesic(a, b).km


df = df.withColumn('DistanceTravelled', geodesic_udf(F.array("lon1", "lat1"), F.array("lon2", "lat2")))
df.createOrReplaceTempView('temp_boating')
df.show()

# COMMAND ----------

# DBTITLE 1,Merge new/updated data back into Aggregate table
# MAGIC %sql
# MAGIC MERGE INTO agg_boating tgt
# MAGIC USING temp_boating src
# MAGIC ON tgt.boat = src.boat and tgt.Timer = src.Timer
# MAGIC WHEN MATCHED 
# MAGIC   AND (tgt.lat1 != src.lat1 OR tgt.lon1 != src.lon1 OR tgt.lat2 != src.lat2 OR tgt.lon2 != src.lon2)
# MAGIC THEN UPDATE
# MAGIC SET tgt.lat1 = src.lat1,  tgt.lon1 = src.lon1, tgt.lat2 = src.lat2, tgt.lon2 = src.lon2, tgt.DistanceTravelled = src.DistanceTravelled
# MAGIC WHEN NOT MATCHED THEN INSERT *

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from agg_boating_2 order by boat,timer
