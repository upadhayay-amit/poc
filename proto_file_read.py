import proto_demo_pb2

# Assuming you have a protobuf file named 'data.pb' in the current directory
protobuf_file = 'data.pb'

# Create an instance of the protobuf message
message = proto_demo_pb2.product()

# Read the protobuf file
with open(protobuf_file, 'rb') as f:
    message.ParseFromString(f.read())

# Access the fields of the protobuf message
print("Field 1:", message.product_name)
print("Field 2:", message.product_id)
print("Field 2:", message.product_desc)
