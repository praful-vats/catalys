from app import create_app

# Create the app instance
app = create_app()

if __name__ == '__main__':
    
    # Run the Flask application with debugging enabled
    app.run(debug=True)
