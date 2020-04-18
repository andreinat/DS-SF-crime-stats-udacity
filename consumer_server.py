from kafka import KafkaConsumer

# Configure Consumer
consumer = KafkaConsumer(bootstrap_servers="localhost:9092",\
                         auto_offset_reset='earliest',\
                         consumer_timeout_ms=1000)

# Set the topic
consumer.subscribe(["police.department.calls.service.log.v1"])

#Print messages consumed
for message in consumer:
    print(message)