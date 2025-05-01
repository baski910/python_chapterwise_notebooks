# to be added
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('my_topic',key=b'my_key',value=b'Hello Kafka')

producer.flush()


from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic',bootstrap_servers='localhost:9092')
for message in consumer:
    print(message)

