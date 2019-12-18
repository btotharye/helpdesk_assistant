# helpdesk_assistant
Basic demo use case showing Rasa X with Service Now API calls to open incidents.

# Setup
Setup a virtualenv of your choice ensuring to use python3 then run the following:

```
source venv/bin/activate
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
deactivate
source venv/bin/activate

export snow_instance=devxxx.service-now.com
export snow_user=user
export snow_pw=password

rasa x
```
**You have to deactivate after installation due to tensorflow and other libraries requiring it to start working**

Also note how we are setting 3 exports, these are used in the script to connect to your service now instance.

`snow_instance` - This is just the instance address, you don't need the leading https.

`snow_user` - The username of the service account this action code will use to open a incident.

`snow_pw` - The password of the service account this action code will use to open a incident.

This will install Rasa X and all the required dependencies.

# Example Conversation Flow
![Rasa Screenshot](https://github.com/btotharye/helpdesk_assistant/blob/master/screenshots/demo_ss.png)
