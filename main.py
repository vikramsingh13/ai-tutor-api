# Import the FastAPI class.
from fastapi import FastAPI
# Import the routes from routers subpackage.
from routers import ai_operations

# Create a FastAPI instance.
app = FastAPI()

# Include the routers.ai_operations routes in our app.
app.include_router(ai_operations.router)

# Default route handler that returns "Hello, World!"
@app.get("/")
def get_root():
  return {"message": "Hello, World!"}