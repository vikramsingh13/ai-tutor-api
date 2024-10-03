from fastapi import FastAPI

# Create a FastAPI instance.
app = FastAPI()

# Default route handler that returns "Hello, World!"
@app.get("/")
def get_root():
  return {"message": "Hello, World!"}