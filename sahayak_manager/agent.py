from google.adk.agents import Agent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm
from .prompt import SAHAYAK_MANAGER
from .sub_agents.knowledge_base_agent.agent import knowledge_base_agent
from .sub_agents.hyper_local_content_agent.agent import hyper_local_content_agent

model = "gemini-2.0-flash"
# model = LiteLlm(model="ollama/gemma3:4b")

root_agent = Agent(
    name="sahayak_manager",
    model=model,
    description="Intelligently routes teacher requests to the right AI agent based on intent—content creation, explanation, or casual interaction.",
    instruction=SAHAYAK_MANAGER,
    sub_agents=[knowledge_base_agent, hyper_local_content_agent]
)