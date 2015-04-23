import pickle
import socket
import struct
import time

LISTEN_URL = ('localhost', 2007)
def send_to_socket(listOfMetricTuples):
    payload = pickle.dumps(listOfMetricTuples, protocol=2)
    header = struct.pack("!L", len(payload))
    message = header + payload
    print message
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(LISTEN_URL)
    sock.sendall(message)
    sock.close()

timestamp = int(time.time())
value = 10.0
name = 'foo.bar.baz'
send_to_socket([(name, (timestamp, value))])
