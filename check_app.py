import vertexai
from vertexai import agent_engines

# Initialize Vertex AI
vertexai.init(project="striped-altar-466108-r2", location="us-central1")

# Get your deployed agent
agent_engine = agent_engines.get('projects/344990955418/locations/us-central1/reasoningEngines/7731651417311543296')

# Create a session and test
session = agent_engine.create_session(user_id="test_user")
for event in agent_engine.stream_query(
    user_id="test_user",
    session_id=session["id"],
    message="Create a story in Hindi about animals for Grade 3"
):
    print(event)