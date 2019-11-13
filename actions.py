# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import http.client 
import json
from Poco.Recommendations import Recommendations
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionColdStart(Action):
     def name(self) -> Text:
         return "action_cold_start"
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print("action cold start")
         tag = tracker.get_slot("tag");
         print("tag --> " + tag)
         recommendation_type = tracker.get_slot("recommendation_type")
         number_of_recommendations = tracker.get_slot("number_of_components")
         if (number_of_recommendations == None):
            number_of_recommendations = 1
         print("recommendation_type --> " + recommendation_type)
         thePayload = self.execute_cold_start(tag,number_of_recommendations)
         recommendations = Recommendations(thePayload)
         dispatcher.utter_message(recommendations.createMessage())
         return []     
     def execute_cold_start(self,tag,number_of_recommendations):
         conn = http.client.HTTPConnection("127.0.0.1:5000")
         payload = ""
         headers = { "cookie": "csrftoken=0XKD8G57k0yz3TE76mlH4UDgIot6SQT8Is4I2dmbQDuVHzuVfxq8r6Cq2XfYwS9z" }
         conn.request("GET", "/resdec/cold_start_features/?relationship_type_id=1&var_environment_id=1&number_recommendations="+ str(number_of_recommendations) +"&selected_features%5B%5D="+tag, payload, headers)
         res = conn.getresponse()
         data = res.read()
         return data.decode("utf-8")

