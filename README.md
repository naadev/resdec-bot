Requires an environment Python 3.7
Before starting, install rasa:
### pip install rasa
After that, you can run NLP Server and/or NLU server
### `rasa run actions`
runs the NLP server
### ' rasa run --cors "*"'
runs the NLU server. 
Be aware of --cors should be set properly to endpoint when run out of a containers or in an unprotected network
