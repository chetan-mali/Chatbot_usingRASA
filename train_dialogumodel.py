import logging, io, json, warnings
logging.basicConfig(level="INFO")
warnings.filterwarnings('ignore')

from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.agent import Agent

agent = Agent('data/domain.yml', policies=[MemoizationPolicy(),KerasPolicy()])
training_data = agent.load_data('data/stories.md')
agent.train(
        training_data,
        validation_split=0.0
)

agent.persist('models/dialogue')
