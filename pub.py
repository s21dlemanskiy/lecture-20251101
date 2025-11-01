from kafka import KafkaProducer


topic = 'test'
publisher = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

## Won't work until we start iteration, so we're using ConsumerRebalanceListener
# assigned_partitions = consumer.assignment()
# print(f"Assigned partitions: {[tp.partition for tp in assigned_partitions]}")

print("Starting Kafka consumer...")
for i in range(10):
    publisher.send(topic, b"Received message: %d" % i)
    publisher.flush()
