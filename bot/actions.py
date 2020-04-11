from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

	
class ActionGreet(Action):
	def name(self):
		return 'action_greet'
		
	def run(self, dispatcher, tracker, domain):
		response = """ආයුබෝවන්"""
						
		dispatcher.utter_message(response)

class ActionBye(Action):
	def name(self):
		return 'action_bye'
		
	def run(self, dispatcher, tracker, domain):
		response = """නැවත හමුවෙමු, ඔබට සුබ දවසක්!"""
						
		dispatcher.utter_message(response)
		
class FindDoc(Action):
	def name(self):
		return 'action_find'
		
	def run(self, dispatcher, tracker, domain):
		response = """ඔබේ ගැටලුව පවසන්න. මම ආයුර්වේද වෙද මහතෙකු සොයා දෙන්නම්"""
						
		dispatcher.utter_message(response)

class injury(Action):
	def name(self):
		return 'action_injury'
		
	def run(self, dispatcher, tracker, domain):
		response = """ඔබේ ආබාධයට මෙම වෙද මහතා හමුවන්න :
                              නම : ආයුර්වේද වෛද්‍ය කමල් පෙරේරා.
                              ලිපිනය : විහාර මාවත, මාලබේ
                              දුරකථන අංකය : 0771234567
"""
						
		dispatcher.utter_message(response)
class location(Action):
	def name(self):
		return 'action_ask_location'
		
	def run(self, dispatcher, tracker, domain):
		response = """ඔබට කුමන ප්‍රදේශයෙන් වෙද මහතෙකු අවශ්‍ය ද?"""
						
		dispatcher.utter_message(response)
		
