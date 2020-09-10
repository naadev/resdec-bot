import http.client 
import json
from Poco.Recommendations import Recommendations


# http://127.0.0.1:5000/resdec/transition_components_based_features/?relationship_type_id=3&var_environment_id=1&algorithm_id=16&username=admin&number_recommendations=1&item_evaluated=platinum-seo-pack
class ResdecServices:
    def execute_cold_start(self,tag,more_components):
             print("CallStartCall -->" + tag + "number of recommendations" + str(more_components))
             conn = http.client.HTTPConnection("127.0.0.1:5000")
             payload = ""
             headers = { "cookie": "csrftoken=0XKD8G57k0yz3TE76mlH4UDgIot6SQT8Is4I2dmbQDuVHzuVfxq8r6Cq2XfYwS9z" }
             conn.request("GET", "/resdec/cold_start_features/?relationship_type_id=1&var_environment_id=1&number_recommendations="+ str(more_components) +"&selected_features%5B%5D="+tag, payload, headers)
             res = conn.getresponse()
             data = res.read()
             return data.decode("utf-8")     
    def execute_feature_based(self,tag, more_components):
             recommendations = self.execute_cold_start(tag,more_components)
             cold_start_recommendations = Recommendations(recommendations)
             recommendedPackage = cold_start_recommendations.getMainRecommendation()
             conn = http.client.HTTPConnection("127.0.0.1:5000")
             payload = ""
             headers = { "cookie": "csrftoken=0XKD8G57k0yz3TE76mlH4UDgIot6SQT8Is4I2dmbQDuVHzuVfxq8r6Cq2XfYwS9z" }
             conn.request("GET","/resdec/transition_components_based_features/?relationship_type_id=3&var_environment_id=1&algorithm_id=16&number_recommendations=1&item_evaluated="+recommendedPackage,payload,headers)
             res = conn.getresponse()
             data = res.read()
             return data.decode("utf-8")
