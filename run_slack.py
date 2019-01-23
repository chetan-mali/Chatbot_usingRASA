from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

interpreter = RasaNLUInterpreter("models/nlu/default/current")
action_endpoint = EndpointConfig(url="http://0.0.0.0:5055/webhook")
agent = Agent.load("models/dialogue", interpreter=interpreter,action_endpoint=action_endpoint)

input_channel = SlackInput(
        slack_token="xoxb-519983005317-523655880211-K1UF8uFBrqWgodJ1nt8fX4zV"
        # this is the `bot_user_o_auth_access_token`
        #slack_channel="YOUR_SLACK_CHANNEL"
            # the name of your channel to which the bot posts (optional)
    )

    # set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=True)
