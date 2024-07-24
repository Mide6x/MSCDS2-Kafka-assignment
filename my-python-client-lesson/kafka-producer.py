import msgpack
import json
from kafka import KafkaProducer

# Msgpack producer
producer2 = KafkaProducer(value_serializer=msgpack.dumps)
producer2.send('msgpack-events', {'msgpack_key': 'msgpack_value'})
producer2.flush()

# JSON producer
producer3 = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer3.send('json-events', {'json_key': 'json_value'})
producer3.flush()
