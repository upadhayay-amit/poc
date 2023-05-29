from confluent_kafka import Consumer
import proto_demo_pb2   # Import your generated protobuf message

# Kafka broker details
bootstrap_servers = 'localhost:9092'
topic = 'test-topic'


def consume_protobuf_messages():
    consumer = Consumer({
        'bootstrap.servers': bootstrap_servers,
        'group.id': 'group2',
        'auto.offset.reset': 'earliest'
    })

    # Subscribe to the Kafka topic
    consumer.subscribe([topic])

    while True:
        # Poll for new messages
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        try:
            # Create an instance of the protobuf message
            message = proto_demo_pb2.product()

            # Deserialize the protobuf message
            message.ParseFromString(msg.value())

            # Access the fields of the protobuf message
            print("product_name:", message.product_name)
            print("product_id:", message.product_id)
            print("product_desc:", message.product_desc)
        except Exception as e:
            print(f"Error processing message: {e}")

    consumer.close()


# Start consuming protobuf messages from Kafka
consume_protobuf_messages()
