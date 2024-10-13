import os
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Set the API key for the OpenAI client
openai.api_key = api_key

# Test OpenAI API call (list available models)
response = openai.Model.list()
print(response)
