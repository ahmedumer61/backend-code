from schema.chatbot_schema import LLMOptions
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


class LLMSelection:
    def __init__(self, model_name: LLMOptions, api_key: str):
        self.model_name = model_name
        self.api_key = api_key
        self.llm = self._select_llm()

    def _select_llm(self):
        """Select and return the appropriate LLM model."""
        if self.model_name == LLMOptions.GROQ:
            return ChatGroq(model="llama-3.1-8b-instant", api_key=self.api_key,
                            )
        elif self.model_name == LLMOptions.GOOGLE_GEMINI:
            return ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=self.api_key)
        elif self.model_name == LLMOptions.OPEN_AI:
            return ChatOpenAI(model="gpt-4o", api_key=self.api_key)
        else:
            raise ValueError("Invalid LLM model selected")
