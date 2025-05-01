from kafka import KafkaProducer
import json
import datetime as dt
import pandas as pd
from time import sleep

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
print(f'Initialized kafka producer at {dt.datetime.now()}')

counter = 0
file = 'online_retail_II.csv'

for chunk in pd.read_csv(file,chunksize=10):
    chunk['InvoiceDate'] = pd.to_datetime(chunk["InvoiceDate"])

    key = str(counter).encode()

    chunkd = chunk.to_dict()

    data = json.dumps(chunkd, default=str).encode('utf-8')

    producer.send(topic='transactions',key=key,value=data)


    sleep(0.5)

    conter = counter + 1

    print(f'Send record to the topic at {dt.datetime.now()}')


###  consumer code   ###

from kafka import KafkaConsumer
import json
import pandas as pd

consumer = KafkaConsumer('transactions',
                         group_id='test-consumer-group',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                         auto_offset_reset='earliest',
                         enable_auto_commit=False)

for message in consumer:
    mframe = pd.DataFrame(message.value)

    mframe['revenue'] = mframe['Quantity']*mframe['Price']

    summary = mframe.groupby('StockCode')['revenue'].sum()

    print(summary)
