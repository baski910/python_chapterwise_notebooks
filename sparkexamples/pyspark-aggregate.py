from pyspark.sql.functions import to_timestamp, sum 
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("StringToDateTime").getOrCreate()
from pyspark.sql.types import StructType,StructField,StringType,FloatType
schema = StructType([
    StructField("index",StringType(),True),
    StructField("date",StringType(),True),
    StructField("duration",FloatType(),False),
    StructField("item",StringType(),True),
    StructField("month",StringType(),True),
    StructField("network",StringType(),True),
    StructField("network_type",StringType(),True),
])
df1 = spark.read.csv('phone_data.csv',header=True,schema=schema)
#df1.show()
df1.printSchema()


#df2 = df1.filter(df1['item']=='call').agg(sum("duration"))
#df3 = df2.agg(sum("duration")).collect()
#df3.show()
#df2 = df1.groupby('item').agg(sum('duration'))
#df2.show()
df2 = df1.where("item=='call'")
df2.show()
