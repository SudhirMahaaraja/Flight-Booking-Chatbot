# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


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
# from datetime import datetime
#
# class ActionFlightSearch(Action):
#     def name(self):
#         return "action_flight_search"
#
#     def run(self, dispatcher, tracker, domain):
#         origin = tracker.get_slot("origin")
#         destination = tracker.get_slot("destination")
#         date = tracker.get_slot("date")
#
#         # You may need to implement logic to validate and parse the date
#         if date:
#             try:
#                 parsed_date = datetime.strptime(date, "%d-%m-%Y").strftime("%d %B %Y")
#             except ValueError:
#                 parsed_date = date
#         else:
#             parsed_date = "today"
#
#         response = f"Here are the available flights from {origin} to {destination} on {parsed_date}:"
#
#         # You can then call an API or database to fetch actual flight information based on origin, destination, and date
#
#         dispatcher.utter_message(response)
#         return []
