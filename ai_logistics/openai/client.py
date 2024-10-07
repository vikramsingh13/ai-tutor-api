"""
  openai/client.py will handle calling the openai services.
"""

# Import os for environment variables.
import os
# Import OpenAI class from openai.
from openai import OpenAI
# Import json for json parsing
import json
# Import load_dotenv for getting environment variables
from dotenv import load_dotenv

# Constant openai gpt model to be used for now.
GPT_MODEL="gpt-3.5-turbo"
# Get the openai api key from environment variables.
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

# Instantiate the OpenAI client with the api key. 
client = OpenAI(
  api_key=OPENAI_API_KEY,
)

def get_chat_response_with_prompt(prompt: str, model: str = GPT_MODEL):
  """
  get_chat_response_with_prompt takes a string param prompt and a string param model which is set to the module's GPT_MODEL constant by default. 
  """

  # Create a chat completion from client.chat.completions with list of messages and model.
  chat_completion = client.chat.completions.create(
    # There could be multiple messages with roles such as "system", "user", etc. 
    messages=[
      {
        "role": "user",
        "content": prompt,
      }
    ],
    model=model,
  )

  # Return the message content from the first choice of the chat completion.
  return chat_completion.choices[0].message.content


