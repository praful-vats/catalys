def process_data(data):

    """
    Processes the given data by converting customer names to uppercase.

    Args:
        data (dict): The original data to be processed.

    Returns:
        dict: The processed data with customer names in uppercase.
    """
    # Iterate over each order and convert the customer name to uppercase
    for order in data['orders']:
        order['customer_name'] = order['customer_name'].upper()
    return data
