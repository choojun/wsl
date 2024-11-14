from kafka import KafkaProducer
import time
import socket

bootstrap_servers = "localhost:9092"
topic = 'cats'
time_interval = 1

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
for num in range(1000000):
    message = f"{num} cats".encode('utf-8')
    print(message.decode('utf-8'))
    producer.send(topic, message)
    time.sleep(time_interval)

producer.flush()
