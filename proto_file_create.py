
import proto_demo_pb2

# Create an instance of the protobuf message
message = proto_demo_pb2.product()
message.product_name = 'iphone'
message.product_id = 1234
message.product_desc = 'iphone 11'

# Write the protobuf message to a file
protobuf_file = 'data.pb'
with open(protobuf_file, 'wb') as f:
    f.write(message.SerializeToString())
