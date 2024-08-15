from flask import Blueprint, jsonify
from .data_processor import process_data
from .storage import store_processed_data, get_stored_data

# Create a blueprint for routing
main_bp = Blueprint('main', __name__)

# Mock data simulating an external service response
mock_data = {
    "orders": [
        {"order_id": 1, "total_price": 100.5, "customer_name": "Singh"},
        {"order_id": 2, "total_price": 200.0, "customer_name": "Rajput"},
        {"order_id": 3, "total_price": 50.75, "customer_name": "Kumar"}
    ]
}

@main_bp.route('/fetch-data', methods=['GET'])
def fetch_data():

    """
    API endpoint that simulates fetching data from an external service,
    processes it, and stores the processed data.

    Returns:
        JSON response with a success message.
    """
     
    # Process the mock data
    processed_data = process_data(mock_data)

    # Store the processed data in memory
    store_processed_data(processed_data)

    # Return a success message
    return jsonify({"message": "Data fetched and processed successfully!"}), 200

@main_bp.route('/get-processed-data', methods=['GET'])
def get_processed_data():

    """
    API endpoint that returns the processed data stored in memory.

    Returns:
        JSON response with the processed data.
    """
    # Retrieve stored data from memory
    data = get_stored_data()

    # Return the processed data
    return jsonify(data), 200
