import json

class Recommendations():
    """Generic class to get an """
    def __init__(self, json_def):
        self.__dict__ = json.loads(json_def)
    def createMessage(self):
        if 'cold_start_recommendations' in self.__dict__:
            if '1' in self.__dict__['cold_start_recommendations']:
                return "It looks you should try "+self.__dict__['cold_start_recommendations']['1']            
        return "I didn't find any feasible recommendation for you"