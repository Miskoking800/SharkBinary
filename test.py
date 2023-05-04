import struct

def save_data(filename, data):
    with open(filename, 'wb') as f:
        for item in data:
            packed_item = struct.pack('ii', item[0], item[1])
            f.write(packed_item)

def load_data(filename):
    data = []
    with open(filename, 'rb') as f:
        while True:
            packed_item = f.read(8)
            if not packed_item:
                break
            item = struct.unpack('ii', packed_item)
            data.append(item)
    return data
