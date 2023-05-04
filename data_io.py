import struct

def save_data(filename, data):
    """
    Save data to a binary file using the struct module.

    Args:
        filename (str): The name of the file to save the data to.
        data (list of tuples): The data to save, where each tuple contains two integers.

    Returns:
        None
    """
    with open(filename, 'wb') as f:
        for item in data:
            packed_item = struct.pack('ii', item[0], item[1])
            f.write(packed_item)

def load_data(filename):
    """
    Load data from a binary file using the struct module.

    Args:
        filename (str): The name of the file to load the data from.

    Returns:
        list of tuples: The loaded data, where each tuple contains two integers.
    """
    data = []
    with open(filename, 'rb') as f:
        while True:
            packed_item = f.read(8)
            if not packed_item:
                break
            item = struct.unpack('ii', packed_item)
            data.append(item)
    return data
