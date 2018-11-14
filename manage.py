import os

from api import create_app
from config import config

config_type = os.getenv('FLASK_ENVIRONMENT', None)

app = create_app(config[config_type])

if __name__ == '__main__':
    
    app.run(debug=True)