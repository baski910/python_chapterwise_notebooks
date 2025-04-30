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

df2 = df1.where("item=='call'")
df2.show()




#filtering
df1 = df1.filter(df1['item']=='call')
df1.show()

# where
df1 = df1.where("item=='call'")
df1.show()
