from enum import Enum


class LLMOptions(str, Enum):
    GROQ = "Groq"
    GOOGLE_GEMINI = "Google Gemini"
    OPEN_AI = "Open-AI"
    

