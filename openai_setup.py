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

if run.status == 'completed':
    # Fetch all messages and filter for the last message from the assistant
    last_message = client.beta.threads.messages.list(
        thread_id=thread.id,
        order='desc',
        limit=1
    )

    # Assuming the variable 'last_message' contains the output
    #last_message_id = last_message.last_id

    # Print the extracted last_id
    #print(f"The last message ID is: {last_message_id}")

    last_message_value = last_message.data[0].content[0].text.value # Access the first (and only) message

    #print(last_message_value)
    # Get the content list of the message
    #content_blocks = message.content

    # Extract the text value from the content
    # Assuming it's the first content block and type is 'text'
    #text_value = content_blocks[0].text.value

    #message = client.beta.threads.messages.retrieve(
        #message_id=last_message_id,
        #thread_id=thread.id ,
    #)
    #print("retriving last message content from its id")
    #last_message_value = message.content[0].text.value
    #print(last_message_value)

    #print(last_message.content[0].text.value)  # Access the first (and only) message in the response

else:
    print("Run status:", run.status)
