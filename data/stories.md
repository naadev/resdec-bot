## interactive_story_1
* greet
    - utter_greet
## help
* help
    - utter_help
* affirm
    - utter_indicator

## Recommendation blueprint

* recommendation_request{"recommendation_type": "Cold Start"}
    - slot{"recommendation_type": "Cold Start"}
    - utter_which_tag
* tags{"tag": "google"}
    - slot{"tag": "google"}
    - utter_summary
	- action_cold_start
> recommendation_blueprint

## a user who wants to know more
> recommendation_blueprint
* more_components{"number_of_components":"1"}
    - slot{"tag": "google"}
    - utter_more_components
	- action_giveme_more
* goodbye OR thank_you
    - utter_goodbye
    - action_restart

    
## a user who wants to know more
> recommendation_blueprint
* goodbye OR thank_you
    - utter_goodbye
    - action_restart

## Want to know more - one
* any_other_platform
    - utter_variability_environment

## bye bye

* goodbye OR thank_you
    - utter_goodbye
    - action_restart

