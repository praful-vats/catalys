def process_data(data):
    for order in data['orders']:
        order['customer_name'] = order['customer_name'].upper()
    return data
