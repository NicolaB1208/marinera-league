
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

import re

message = client.beta.threads.messages.retrieve(
        message_id='msg_Ii11VIzeJCW3oDGtUywZG2FM',
        thread_id='thread_oe02quVOW6Fp1cC22f2kfcr6',
    )
#print("retriving last message content from its id")
#print(message.content[0].text.value)

# Assuming last_message_value contains the message content
last_message_value = message.content[0].text.value

# Use regular expression to find content between triple backticks and newlines
pattern = r"```(?:\n)([\s\S]*?)(?:\n)```"

# Search for the pattern
match = re.search(pattern, last_message_value)

if match:
    # Extract the content found between triple backticks and newlines
    extracted_content = match.group(1)
    print(extracted_content)  # You can print or save the extracted content to a variable
    print(type(extracted_content))
else:
    print("No content found between triple backticks and newlines")

output_file_path='source-files/2024/cl-madrid/ai-results/eliminatoria/ai_processed_adulto_automatic.csv'

write_string_to_csv(extracted_content,output_file_path)