from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    action_endpoint = EndpointConfig(url="http://0.0.0.0:5055/webhook")
    agent = Agent.load("models/dialogue", interpreter=interpreter,action_endpoint=action_endpoint)
    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        responses = agent.handle_text(input())
        for response in responses:
            print(response["text"])
    return agent


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    utils.configure_colored_logging(loglevel="INFO")
    run()
