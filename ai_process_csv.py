# These line is like getting the tools we need from a toolbox. We're grabbing what we need from OpenAI to talk to its AI models.
from openai import OpenAI
import os
from dotenv import load_dotenv
from functions import read_csv_as_string

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
print(f"New chat session (thread) created with ID: {thread.id}")

# Path to your CSV file
csv_file_path = 'source-files/2024/cl-madrid/eliminatoria/adulto.csv'

# Get the entire CSV content as a string
csv_content = read_csv_as_string(csv_file_path)

csv_content = f"```\n{csv_content}\n```"

print(csv_content)

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

    # Assuming the variable 'last_message' contains the output
    last_message_id = last_message.last_id

    # Print the extracted last_id
    print(f"The last message ID is: {last_message_id}")

    last_message_value = last_message.data[0].content[0].text.value # Access the first (and only) message

    print(last_message_value)
    # Get the content list of the message
    #content_blocks = message.content

    # Extract the text value from the content
    # Assuming it's the first content block and type is 'text'
    #text_value = content_blocks[0].text.value

    message = client.beta.threads.messages.retrieve(
        message_id=last_message_id,
        thread_id=thread.id ,
    )
    print("retriving last message content from its id")
    print(message.content[0].text.value)

    #print(last_message.content[0].text.value)  # Access the first (and only) message in the response

else:
    print("Run status:", run.status)