from rasa_core.agent import Agent
from IPython.display import IFrame

agent = Agent.load('models/dialogue')
agent.visualize("stories.md", "story_graph.html", max_history=2)

IFrame(src="./story_graph.html", width=1000, height=800)