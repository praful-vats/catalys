# Flask Data Retrieval and Processing System

## Overview
This is a simplified Flask application that simulates data retrieval, processing, and storage. The application exposes two API endpoints:

1. `/fetch-data`: Fetches and processes mock data.
2. `/get-processed-data`: Returns the processed data stored in memory.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd flask_app
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask application:
    ```bash
    python run.py
    ```

6. Access the API endpoints:
    - Fetch and process data: [http://127.0.0.1:5000/fetch-data](http://127.0.0.1:5000/fetch-data)
    - Get processed data: [http://127.0.0.1:5000/get-processed-data](http://127.0.0.1:5000/get-processed-data)

## Testing
Run the following command to execute tests:
```bash
python -m unittest discover -s tests
