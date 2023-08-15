import json
import time

logs = {}

class CircularBuffer:
    def __init__(self, max_size):
        self.max_size = max_size
        self.length = 0
        self.ptr = 0
        self.buf = [0] * max_size

    def append(self, val):
        self.buf[self.ptr] = val
        self.ptr += 1
        if self.ptr == self.max_size:
            self.ptr = 0
        if self.length < self.max_size:
            self.length += 1

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError('list index out of range')
        index += self.ptr - self.length
        if index < 0:
            index += self.length
        return self.buf[index]

    def __iter__(self):
        for i in range(self.length):
            yield self[i]


def init(topic, size):
    logs[topic] = CircularBuffer(size)

def handle_request(ioty_mqtt, topic, msg):
    if topic not in logs:
        return
    req = json.loads(msg)
    if req['type'] == 'request_all':
        send_all(ioty_mqtt, topic)

def send_all(ioty_mqtt, topic):
    data = {
        'type': 'data_all',
        'data': tuple(logs[topic])
    }
    data = json.dumps(data)
    data = bytes(data, 'utf-8')
    ioty_mqtt.publish(bytes(topic + '_app', 'utf-8'), data)

def log(ioty_mqtt, topic, data):
    if topic not in logs:
        return
    logs[topic].append(data)
    data = {
        'type': 'data_some',
        'data': [data]
    }
    data = json.dumps(data)
    data = bytes(data, 'utf-8')
    ioty_mqtt.publish(bytes(topic + '_app', 'utf-8'), data)

def log_with_time(ioty_mqtt, topic, data):
    log(ioty_mqtt, topic, (time.time() + 946684800, data))
