#-------------------------------------------------------------
from rasa_core.agent import Agent
agent = Agent.load('models/dialogue', interpreter='projects/nlu/default/model')
#-----------------------------------------------------------------
import warnings
warnings.filterwarnings('ignore')
print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    a = input("<User>:")
    if a == 'stop':
        break
    responses = agent.handle_text(a)
    for response in responses:
        print("<-Bot>:",response["text"])