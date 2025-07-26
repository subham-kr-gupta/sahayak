from google.adk.agents import Agent
from .prompt import KNOWLEDGE_BASE_PROMPT
# from google.adk.tools import google_search
from google.adk.models.lite_llm import LiteLlm

model = "gemini-2.0-flash"
# model = LiteLlm(model="ollama/gemma3:4b")

knowledge_base_agent = Agent(
    name="knowledge_base_agent",
    model=model,
    description="Provides simple, analogy-rich explanations for complex student questions in the teacher’s preferred language.",
    instruction=KNOWLEDGE_BASE_PROMPT,
    # output_key="final_answer"
    # tools=[google_search],
)