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

def get_chat_response_with_prompt(user_prompt: str, model: str = GPT_MODEL):
  """
  get_chat_response_with_prompt takes a string param prompt and a string param model which is set to the module's GPT_MODEL constant by default. 
  """
  # Construct the prompt from the user_prompt and template.
  prompt = construct_prompt_from_no_context_template(no_context_template, json_example, user_prompt)

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

  print(chat_completion.choices[0].message.content)

  # Return the message content from the first choice of the chat completion.
  return chat_completion.choices[0].message.content
  


# TODO: refactor these to utils, templates, etc.
context_template = "Context information is below.\n---------------------\n{}\n---------------------\nCourse content example JSON:\n---------------------\n{}\n---------------------\nGiven the context information, example JSON structure, and not using prior knowledge, answer the query with a course content JSON. Answer should only contain a JSON output and nothing else.\nQuery: {}\nAnswer:\n"

no_context_template = "Your task is to help create a course from any given context and user query. Course content example JSON structure:\n---------------------\n{}\n---------------------\nGiven the example JSON structure, answer the user query with a course content JSON with 5 modules and each module containing 3 sub modules. The sub module content should have enough text to help the user learn the concept mentioned in the heading. Answer should only contain a JSON output with course content related to the query and nothing else. Make sure the answer JSON is one long string with no newline, tab, etc, characters. \nQuery: {}\nAnswer:\n"

json_example = """{"courseTopic":"Computers","modules":{"1":{"title":"Title 1","description":"description 1","subModules":{"1":{"heading":"Sub Module 1","content":"content"},"2":{"heading":"Sub Module 2","content":"content"}}},"2":{"title":"Title 1","description":"description 1","subModules":{"1":{"heading":"Sub Module 1","content":"content"},"2":{"heading":"Sub Module 2","content":"content"}}}}}"""


def construct_prompt_from_no_context_template(template: str, examples: str, user_prompt: str):
  return template.format(examples, user_prompt)



