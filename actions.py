# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from Services.resdecservices import ResdecServices
from Poco.Recommendations import Recommendations
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# http://127.0.0.1:5000/resdec/transition_components_based_features/?relationship_type_id=3&var_environment_id=1&algorithm_id=16&username=admin&number_recommendations=1&item_evaluated=platinum-seo-pack

    

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
         more_components = tracker.get_slot("number_of_components")
         print("Number of recommendations --> " + str(more_components))
         if (more_components == None):
            more_components = 1
         print("recommendation_type --> " + recommendation_type)
         operations = ResdecServices()
         if recommendation_type == 'Cold Start':
             thePayload = operations.execute_cold_start(tag,more_components)
             recommendations = Recommendations(thePayload)
             recommendations.createMessage(dispatcher)
         else:
             thePayload = operations.execute_feature_based(tag,more_components)
             recommendations = Recommendations(thePayload)
             recommendations.createMessage(dispatcher)
         return []     

class DefaultActionColdStart(Action):
     def name(self) -> Text:
         return "action_giveme_more"
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print("give me more")
         tag = tracker.get_slot("tag");
         print("tag --> " + tag)
         recommendation_type = tracker.get_slot("recommendation_type")
         more_components = tracker.get_slot("number_of_components")
         if (more_components == None):
            more_components = 1
         print("recommendation_type --> " + recommendation_type)
         operations = ResdecServices()
         if recommendation_type == 'Cold Start':
               thePayload = operations.execute_cold_start(tag,more_components)
               recommendations = Recommendations(thePayload)
               recommendations.createAlternatives(dispatcher)
         else :
               thePayload = operations.execute_feature_based(tag,more_components)
               recommendations = Recommendations(thePayload)
               recommendations.createAlternatives(dispatcher);
         return []     