# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text, Union, Optional
from rasa_sdk.events import SlotSet
import requests
#
#
class SetSlot(Action): 
    "Sets the policy type slot"

    def name(self) -> Text:
        return "action_set_policy_type"
    
    def run(self, dispatcher, tracker, domain):    
        current_intent = tracker.latest_message['intent'].get('name')
#        current_entity = tracker.latest_message['entities'].get('name')
        if current_intent == "about_leave" or current_intent == "about_leave_types" or current_intent == "numberof_leave" or current_intent == "leave_benefits" or current_intent == "weekend_counted":
            policy_type ="leave_policy"
        elif current_intent == "about_maternity_benefits" or current_intent == "maternity_counted" or current_intent == "maternity":
            policy_type= "maternity_leave_policy"
        elif current_intent == "paternity_benefit" or current_intent == "paternity_counted" or current_intent == "about_paternity":
            policy_type= "paternity_leave_policy"
        elif current_intent == "employee_cafeteria_policy":
            policy_type= "cafeteria_policy"
        else:
            policy_type = tracker.get_slot("policy_type") 
        return [SlotSet("policy_type", policy_type )]