storage = {}

def store_processed_data(data):
    global storage
    storage = data

def get_stored_data():
    return storage
