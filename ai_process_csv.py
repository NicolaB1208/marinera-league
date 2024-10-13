from openai import OpenAI
import os
from dotenv import load_dotenv
from functions import read_csv_as_string,write_string_to_csv
import re

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

# Step 1-B: Retrieve an already created assistant using its id
assistant = client.beta.assistants.retrieve('asst_0urRZRs0q9ZotCxpirCrfwpQ')

# Step 2: Start a new chat session, by creating a new thread
thread = client.beta.threads.create()
#print(f"New chat session (thread) created with ID: {thread.id}")

# Categories list
folder_path = "source-files/2024/cl-madrid/eliminatoria"
file_list = os.listdir(folder_path)
categories = [os.path.splitext(file)[0] for file in file_list]

for category in categories:
    # Path to your CSV file
    csv_file_path = 'source-files/2024/cl-madrid/eliminatoria/' + category + '.csv'

    # Get the entire CSV content as a string
    csv_content = read_csv_as_string(csv_file_path)

    csv_content = f"```\n{csv_content}\n```"

    print(category + '.csv loaded as string')

    # Step 3: Add your message to the chat session
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=csv_content
    )
    last_user_message_created_at = message.created_at

    # Step 4: Call the model to get a response
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    if run.status == 'completed':
        # Fetch all messages and filter for the last message from the assistant
        last_message = client.beta.threads.messages.list(
            thread_id=thread.id,
            order='desc',
            limit=1
        )

        last_message_value = last_message.data[0].content[0].text.value # Access the first (and only) message
    else:
        print("Run status:", run.status)

    # Use regular expression to find content between triple backticks and newlines
    pattern = r"```(?:\n)([\s\S]*?)(?:\n)```"

    # Search for the pattern
    match = re.search(pattern, last_message_value)

    if match:
        # Extract the content found between triple backticks and newlines
        extracted_content = match.group(1)
        print('   extracted content from AI response')  # You can print or save the extracted content to a variable
    else:
        print("No content found between triple backticks and newlines")

    output_file_path='source-files/2024/cl-madrid/ai-results/eliminatoria/ai_processed_' + category + '.csv'

    write_string_to_csv(extracted_content,output_file_path)

    print('   ai_processed CSV created\n')

print('AI processed all the files in '+ folder_path)