from flask import Flask

def create_app():

    """
    Factory function to create and configure the Flask application.

    Returns:
        Flask app instance.
    """
    
    app = Flask(__name__)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
