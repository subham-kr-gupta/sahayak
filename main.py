import vertexai
from vertexai import agent_engines
from sahayak_manager.agent import root_agent

# remote_app = agent_engines.create(
#     agent_engine=root_agent,
#     requirements=[
#         "google-cloud-aiplatform[adk,agent_engines]",
#     ]
# )

PROJECT_ID = "striped-altar-466108-r2"
LOCATION = "asia-south1"
STAGING_BUCKET = "gs://coactivators-sahayak-gcs-bucket"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

from vertexai.preview import reasoning_engines

app = reasoning_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

session = app.create_session(user_id="u_123")
session


for event in app.stream_query(
    user_id="u_123",
    session_id=session.id,
    message="Generate a poem for rain in marathi",
):
    print(event)