
# These line is like getting the tools we need from a toolbox. We're grabbing what we need from OpenAI to talk to its AI models.
from openai import OpenAI
import os
from dotenv import load_dotenv
from functions import read_csv_as_string,write_string_to_csv


# Load environment variables from the .env file
load_dotenv()

# Access the keys
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("ORG_ID")
project_id = os.getenv("PROJECT_ID")

# We start by connecting to OpenAI's services with something like a phone dialing a number to start a conversation.
client = OpenAI(
  organization=org_id,
  project=project_id,
)

# Path to your CSV file
#csv_file_path = 'source-files/2024/cl-madrid/ai-results/eliminatoria/ai_processed_adulto.csv'

# Get the entire CSV content as a string
#csv_content = read_csv_as_string(csv_file_path)

#csv_content = f"```\n{csv_content}\n```"

#print(csv_content)

import os

# Example usage
folder_path = "source-files/2024/cl-madrid/eliminatoria"
file_list = os.listdir(folder_path)
categories = [os.path.splitext(file)[0] for file in file_list]

print(categories)
