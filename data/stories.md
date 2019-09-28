## interactive_story_1
* greet
    - utter_greet
## help
* help
    - utter_help
* affirm
    - utter_indicator

## a user who knows

* recommendation_request{"recommendation_type": "Cold Start"}
    - slot{"recommendation_type": "Cold Start"}
    - utter_which_tag
* tags{"tag": "google"}
    - slot{"tag": "google"}
    - utter_summary_cold_start

## bye bye

* goodbye
    - utter_goodbye
    - action_restart

