# -*- coding: utf-8 -*-
import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text, Union, Optional
import json
from rasa_sdk.events import SlotSet
import requests

logger = logging.getLogger(__name__)

class SetSlot(Action): 
    "Sets the policy type slot"

    def name(self) -> Text:
        return "action_set_policy_type"
    
    def run(self, dispatcher, tracker, domain):    
        current_intent = tracker.latest_message['intent'].get('name')
#        current_entity = tracker.latest_message['entities'].get('name')
        if current_intent == "about_leave" or current_intent == "about_leave_types" or current_intent == "leave_entitement" or current_intent == "leave_benefits" or current_intent == "weekend_counted":
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
    
class ResetSlot(Action):
    "resets the LWP Slot to None"

    def name(self) -> Text:
        return "action_reset_LWP_slot"

    def run(self, dispatcher, tracker, domain):  
        return [SlotSet("leave_type", None)]

class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        #self.intent_mappings = pd.read_csv("demo/intent_description_mapping.csv")
        #self.intent_mappings.fillna("", inplace=True)
        #self.intent_mappings.entities = self.intent_mappings.entities.map(
        #    lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        first_intent_names = [
            intent.get("name", "")
            for intent in intent_ranking
            if intent.get("name", "") != "out_of_scope"
        ]

        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            logger.debug(intent)
            logger.debug(entities)
            buttons.append(
                {
                    "title": self.get_button_title(intent, entities),
                    "payload": "/{}{}".format(intent, entities_json),
                }
            )

        # /out_of_scope is a retrieval intent
        # you cannot send rasa the '/out_of_scope' intent
        # instead, you can send one of the sentences that it will map onto the response
        buttons.append(
            {
                "title": "Something else",
                "payload": "I am asking you an out of scope question",
            }
        )

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []

        class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in [
            "ask_builder",
            "ask_howdoing",
            "ask_whatspossible",
            "ask_whatisiona",
            "ask_isbot",
            "ask_howold",
            "ask_wherefrom",
            "ask_whoami",
            "handleinsult",
            "nicetomeeyou",
            "telljoke",
            "ask_whatismyname",
            "ask_howbuilt",
            "ask_whoisit",
        ]:
            dispatcher.utter_message(template=f"utter_{intent}")
        return []
        
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # Fallback caused by TwoStageFallbackPolicy
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_message(template="utter_restart_with_button")

            return [SlotSet("feedback_value", "negative"), ConversationPaused()]

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_default")
            return [UserUtteranceReverted()]


