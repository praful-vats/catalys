from flask import Blueprint, jsonify
from .data_processor import process_data
from .storage import store_processed_data, get_stored_data

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
    processed_data = process_data(mock_data)
    store_processed_data(processed_data)
    return jsonify({"message": "Data fetched and processed successfully!"}), 200

@main_bp.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    data = get_stored_data()
    return jsonify(data), 200
