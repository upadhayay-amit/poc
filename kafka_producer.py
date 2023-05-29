
from confluent_kafka import Producer
import proto_demo_pb2 # Import your generated protobuf message

# Kafka broker details
bootstrap_servers = 'localhost:9092'
topic = 'test-topic'


def publish_protobuf_message(protobuf_message):
    producer = Producer({'bootstrap.servers': bootstrap_servers})

    # Serialize the protobuf message
    serialized_message = protobuf_message.SerializeToString()

    # Publish the message to Kafka
    producer.produce(topic=topic, value=serialized_message)
    producer.flush()

# Create an instance of your protobuf message

message =  proto_demo_pb2.product()
message.product_name = 'android'
message.product_id = 4321
message.product_desc = 'samsung s2'

message.product_name = 'xbox'
message.product_id = 4324
message.product_desc = 'gaming xbox'

# Publish the protobuf message to Kafka
publish_protobuf_message(message)

