import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GALLEY_API_KEY')
api_url = os.getenv('GALLEY_URL')
max_retries = 2
