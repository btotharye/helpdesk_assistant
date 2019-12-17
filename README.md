# helpdesk_assistant
Basic demo use case showing Rasa X with Service Now API calls to open incidents.

# Setup
Setup a virtualenv of your choice ensuring to use python3 then run the following:

```
source venv/bin/activate
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
deactivate
source venv/bin/activate
```
**You have to deactivate after installation due to tensorflow and other libraries requiring it to start working**

This will install Rasa X and all the required dependencies.