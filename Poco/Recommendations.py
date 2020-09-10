import json
from rasa_sdk.executor import CollectingDispatcher

class Recommendations():
    """Generic class to get an """
    def __init__(self, json_def):
        self.__dict__ = json.loads(json_def)
    def getMainRecommendation(self):
        if 'cold_start_recommendations' in self.__dict__:
            if '1' in self.__dict__['cold_start_recommendations']:
                return self.__dict__['cold_start_recommendations']['1']     
        if 'tran_comp_featuring_recommendation' in self.__dict__:
            if '1' in self.__dict__['tran_comp_featuring_recommendation']:
                return self.__dict__['tran_comp_featuring_recommendation']['1']    
        return None
    def createMessage(self,dispatcher: CollectingDispatcher):
        recommendation = self.getMainRecommendation()
        if recommendation != None:
                dispatcher.utter_message("It looks you should try ")
                dispatcher.utter_message(">>"+recommendation)
                return
        dispatcher.utter_message("I didn't find any feasible recommendation for you")
        return
    def createAlternatives(self,dispatcher: CollectingDispatcher):
        dictLen = len(self.__dict__['possible_interest_recommendations'])      
        if dictLen > 1:
            dispatcher.utter_message("you can try also with:\n")
            for iloop in range(1,(dictLen+1)): 
                dispatcher.utter_message('>>'+self.__dict__['possible_interest_recommendations'][str(iloop+1)])
            return
        dispatcher.utter_message("I don't have any other component to recommend you")
        return