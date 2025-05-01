from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType



spark = SparkSession.builder.appName("CSVtoKafka").getOrCreate()

# Define the schema of the data to write to Kafka


schema = StructType([
    StructField("index", StringType(), True),
    StructField("date", StringType(), True),
    StructField("duration", StringType(), True),
    StructField("item", StringType(), True),
    StructField("month", StringType(), True),
    StructField("network", StringType(), True),
    StructField("network_type", StringType(), True),
])


csv_file_path = "phone_data.csv"
df = spark.read.csv(csv_file_path, header=True,schema=schema)

#df_string = df.toJSON().toDF(schema=schema)
#df_string = df.selectExpr("to_json(struct(*)) as value")

#val data = Seq(("key1", "value1"), ("key2", "value2"))
#val df = spark.createDataFrame(data).toDF("key", "value")
#data = [("key1", "value1"), ("key2", "value2")]
#df = spark.createDataFrame(data).toDF("key", "value")

#df.selectExpr("CAST(key AS STRING) AS key", "CAST(value AS STRING) AS value") \

df.selectExpr("to_json(struct(*)) as value").write.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "csv_topic") \
    .save()


##### consumer code ###############
import requests
import json
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CSVtoKafka").getOrCreate()

kafka_df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "csv_topic") \
    .load()

kafka_df_string = kafka_df.selectExpr("CAST(value AS STRING)")

def send_to_flask(batch_df, batch_id):
    data = batch_df.toJSON().collect()
    for row_json in data:
        try:
            row_dict = json.loads(row_json)
            print(row_dict)
            requests.post('http://localhost:5000/data', json=row_dict)
        except json.JSONDecodeError:
            print(f"Error decoding JSON: {row_json}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

kafka_df_string.writeStream.foreachBatch(send_to_flask).start().awaitTermination()


#####  flask app   ###
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(f"Received data: {data}")
    return jsonify({"message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
