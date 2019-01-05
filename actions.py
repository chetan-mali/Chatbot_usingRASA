from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class Actioneligibility(Action):
	def name(self):
		return 'action_eligibility'
		
	def run(self, dispatcher, tracker, domain):
						
		dispatcher.utter_message("XXXXXXXX")
		return

