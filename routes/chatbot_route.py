from fastapi import APIRouter, HTTPException, status, Form
from services.langchain_services.chatbot import ChatBot
from services.langchain_services.model import LLMSelection
from schema.chatbot_schema import LLMOptions
from schema.workout_schema import WorkOutSchema
from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

router = APIRouter()


@router.post("/chatbot",status_code=status.HTTP_200_OK)
def chat_router(
    llm: LLMOptions = Form(default=LLMOptions.GROQ),
    bmi:float=Form(...),
    workout: WorkOutSchema = Form(...),
):
    try:
        # Initialize the LLM selection
        llm_model = LLMSelection(llm, api_key)
        # Initialize the ChatBot with the correct session manager
        bot = ChatBot(llm_model, api_key)

        # Generate response using the ChatBot
        response = bot.generate_response(bmi=bmi,
                                         workout=workout)
        # response_dict = response.dict()
        return {"response": response}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}",
        )
