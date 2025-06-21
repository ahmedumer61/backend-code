from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chatbot_route

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot_route.router)

# FAstapi for web server APIs==>Python web framework.
# uvicorn main:app --reload
