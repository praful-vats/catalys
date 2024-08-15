storage = {}

def store_processed_data(data):

    """
    Stores the processed data in the global in-memory storage.

    Args:
        data (dict): The processed data to be stored.
    """
    global storage
    storage = data

def get_stored_data():

    """
    Retrieves the stored data from memory.

    Returns:
        dict: The stored processed data.
    """
    return storage
