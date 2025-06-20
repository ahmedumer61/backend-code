from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from datetime import date
from langchain_core.prompts import ChatPromptTemplate
from services.langchain_services.model import LLMSelection
from services.langchain_services.prompts import PROMPT
from schema.output_schema import HealthPlan


class SessionManager:
    def __init__(self):
        self.store = {}
        self._date = date.today()
        self._datekey = str(self._date)

    def get_session_history(self, session_id: str = None) -> BaseChatMessageHistory:
        """Get or create a session's message history with a default session ID."""
        if session_id is None:
            session_id = (
                self._datekey
            )  # Use the default session ID based on the current date

        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]


class ChatBot:
    def __init__(
        self, model: LLMSelection, api_key: str, session_manager: SessionManager = None
    ):
        self.model = model
        self.api_key = api_key
        self.session_manager = (
            session_manager or SessionManager()
        )  # Default session manager

    def generate_response(self,
                          bmi:float,
                          workout: str,
                          session_id: str = None
                          ) -> str:
        """Generate a response from the selected LLM model based on the message."""
        # Use the default session history if none is provided
        session_history = self.session_manager.get_session_history(session_id)

        # Create prompt with message
        prompt = ChatPromptTemplate.from_template(PROMPT).format(
            bmi=bmi,
            workout=workout,
        )

        # Initialize the model with memory
        model_with_memory = RunnableWithMessageHistory(
            self.model.llm.with_structured_output(HealthPlan), self.session_manager.get_session_history
        )

        # Send message to model
        response = model_with_memory.invoke(
            prompt,
            config={
                "configurable": {
                    "session_id": session_id or self.session_manager._datekey
                }
            },
        )
        return response
