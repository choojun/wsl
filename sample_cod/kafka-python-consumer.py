from kafka import KafkaConsumer
import socket

bootstrap_servers = "localhost:9092"
topic = 'cats'

consumer = KafkaConsumer(topic,bootstrap_servers=bootstrap_servers)

for msg in consumer:
    print(msg)

