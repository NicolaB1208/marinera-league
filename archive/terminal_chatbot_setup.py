# Create the space where you will type your message
query = input("You: ")
while query.lower() != 'exit':
    
  # Step 3: Add your message to the chat session
  message = client.beta.threads.messages.create(
      thread_id=thread.id,
      role="user",
      content=query
  )
  last_user_message_created_at = message.created_at

  # Step 4: Call the model to get a response
  run = client.beta.threads.runs.create_and_poll(
      thread_id=thread.id,
      assistant_id=assistant.id,
      # instructions="Please address the user as Nicola. The user has a premium account."
  )

  # Step 5: Show the response of the model
  if run.status == 'completed':
    # Fetch all messages and filter for the last message from the assistant
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    # Filtering for assistant's messages
    assistant_messages = [msg for msg in messages.data if msg.role == 'assistant']
    if assistant_messages:
        for message in reversed(assistant_messages):
            # Access the 'created_at' attribute of each message
            if message.created_at > last_user_message_created_at:
                # print the assistant message
                last_assistant_message_text = message.content[0].text.value
                print("\n")
                print(f"Assistant: {last_assistant_message_text}")
                print("\n")
    else:
        print("No messages from the assistant.")
  else:
    print("Run status:", run.status)

  # Ask to type a new message that will initiate the previous loop again
  query = input("You: ")
# When the user types 'exit', the program will end.
print("Goodbye!")


