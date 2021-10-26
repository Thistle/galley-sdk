
import os
import importlib

# instantiation of package dependencies that are only required for local development.
dotenvlib = importlib.find_loader('dotenv')
if dotenvlib is not None:
    from dotenv import load_dotenv
    load_dotenv()

api_key = os.getenv('GALLEY_API_KEY')
api_url = os.getenv('GALLEY_URL')
max_retries = 2
