from google.adk.agents import Agent, LlmAgent
from google.adk.models.lite_llm import LiteLlm
# from google.adk.tools import google_search
from .prompt import HYPER_LOCAL_CONTENT_PROMPT

model = "gemini-2.0-flash"
# model = LiteLlm(model="ollama/gemma3:4b")

hyper_local_content_agent = LlmAgent(
    name="hyper_local_content_agent",
    model=model,
    description="Creates culturally relevant, grade-appropriate educational content in local languages based on the teacher’s request.",
    instruction=HYPER_LOCAL_CONTENT_PROMPT,
    # output_key="assistant_answer",
    # tools=[google_search],
)