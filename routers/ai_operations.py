"""
ai_operations.py contains routes related to all the AI operations including course content generation, document extraction/summarization, vectorization/text embeddings, AI-as-judge, etc.
"""

# Import the APIRouter from fastapi.
from fastapi import APIRouter
# Import openai client module as openai_client
from ..ai_logistics.openai import client as openai_client

# Instantiate the APIRouter.
# Usage of APIRouter and it's syntax is similar in structure to the FastAPI instance.
# Add custom tags, prefix, etc. 
router = APIRouter(
  tags=["ai-operations"],
  prefix="/ai-operations",
  dependencies=[],
  responses={403: {"description": "API key invalid."}}
)


@router.get("/course-generation/{prompt}")
def generateCourseFromDescription(prompt: str):
  """
  generateCourseFromDescription returns a JSON containing content for the course modules and submodules. 
  """
  # Get the course content from our openai_client module.
  # The function returns a JSON.
  course_content = openai_client.get_chat_response_with_prompt(prompt)

  # Return the JSON response.
  return course_content