from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('local').getOrCreate()
rdd = spark.sparkContext.textFile("test.txt")


#for element in rdd.collect():
#    print(element)

# flatMap transformation flattens the RDD after applying the function and returns t
# the new RDD. flatMap is similar to map but with one difference, each input can 
# map to zero or more output
rdd2 = rdd.flatMap(lambda x: x.split(" "))

for element in rdd2.collect():
    print(element)

# map transformation is used to apply a function to each element
rdd3 = rdd2.map(lambda x: (x,1))
for element in rdd3.collect():
    print(element)

# reduceByKey merges the value for each key with function 

rdd4 = rdd3.reduceByKey(lambda a,b: a+b)
for element in rdd4.collect():
    print(element)
