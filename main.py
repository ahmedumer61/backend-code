from fastapi import FastAPI
from routes import chatbot_route

app = FastAPI()

app.include_router(chatbot_route.router)

#FAstapi for web server APIs==>Python web framework.
# uvicorn main:app --reload
