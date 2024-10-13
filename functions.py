from openai import OpenAI
import json
import csv
from io import StringIO

# Function to read the entire CSV and format it as a string
def read_csv_as_string(input_file_path):
    output = StringIO()
    with open(input_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(output)

        # Write each row into the StringIO buffer
        for row in reader:
            writer.writerow(row)
    
    # Return the CSV content as a string
    return output.getvalue()

def write_string_to_csv(csv_string,output_file_path):
    # Use StringIO to treat the csv_string as a file-like object
    input_data = StringIO(csv_string)
    reader = csv.reader(input_data)

    # Write the content to the output CSV file
    with open(output_file_path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write each row from the csv_string to the file
        for row in reader:
            writer.writerow(row)


client = OpenAI()

# print thread messages in a structured json
def print_thread_to_json(thread_id):
  messages = client.beta.threads.messages.list(
    thread_id=thread_id
  )
  # print messages
  # print(f"All messages: {messages.data}")
  
  # Prepare to write the data to a file in a structured way
  with open('structured_messages_output.json', 'w') as file:
    structured_data = []
    for message in messages.data:
        # Extract and structure the content of each message using attribute access
        formatted_message = {
            "id": message.id,
            "role": message.role,
            "content": message.content[0].text.value if message.content else 'No content',
            "created_at": message.created_at,
            "assistant_id": getattr(message, 'assistant_id', 'None')  # Safe access with default if attribute missing
        }
        structured_data.append(formatted_message)
    
    # Convert the list of structured data to a JSON formatted string
    json_data = json.dumps(structured_data, indent=4)
    
    # Write the JSON data to the file
    file.write(json_data)