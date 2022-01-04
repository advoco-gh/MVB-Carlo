# **************************************************************************************
# WARNING: This is a static file, useful as a starting point. You may want to change it.
# **************************************************************************************

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for an assistant that schedules reminders and
# reacts to external events.

# class MyCustomAction(Action):
#     def name(self) -> Text:
#         return "action_name"
#     async def run(
#         self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = tracker.events

        rejections_counter = 0

        for x in a:
            if x['event'] == 'user':
                if x['parse_data']['intent']['name'] == 'reject':
                    rejections_counter += 1

        if rejections_counter == 1:
            mx = 'okay I understand this may not be a top priority right now, or perhaps you don’t see the value in it.many people have said the same, but once my manager meet them up and guide along with the nomination they find it very useful to have this settle before hand.allow me to have  two minutes of your time and I promise you’ll be clear on whether or not this is a good use of your time.'
        else :
            mx = 'okay thank you have a nice day. Goodybye!'

        dispatcher.utter_message(text=mx)

        return []