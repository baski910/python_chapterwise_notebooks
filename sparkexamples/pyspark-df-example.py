columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

# create a Spark RDD from a collection List by calling parallelize() function from SparkContext 

spark = SparkSession.builder.appName('myApp').getOrCreate()
rdd = spark.sparkContext.parallelize(data)

# PySpark RDD’s toDF() method is used to create a DataFrame from the existing RDD. 
# Since RDD doesn’t have columns, 
# the DataFrame is created with default column names “_1” and “_2” as we have two columns.

dfFromRDD1 = rdd.toDF()
dfFromRDD1.printSchema()  # displays the schema

# customize the schema
columns = ["language","users_count"]
dfFromRDD1 = rdd.toDF(columns)
dfFromRDD1.printSchema()

# create dataframe using schema
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
data2 = [("James","","Smith","36636","M",3000),
    ("Michael","Rose","","40288","M",4000),
    ("Robert","","Williams","42114","M",4000),
    ("Maria","Anne","Jones","39192","F",4000),
    ("Jen","Mary","Brown","","F",-1)
  ]

schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ])
 
df = spark.createDataFrame(data=data2,schema=schema)
df.printSchema()
df.show(truncate=False)





