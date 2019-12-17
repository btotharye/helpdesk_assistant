from typing import Dict, Text, Any, List, Union, Optional
import datetime
import logging
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import Form

import requests
import json
import os

snow_user = os.getenv("snow_user")
snow_pw = os.getenv("snow_pw")

def email_to_sysid(email):
    lookup_url = 'https://dev79101.service-now.com/api/now/table/sys_user?sysparm_limit=1&email={}'.format(email)
    user = snow_user
    pwd = snow_pw
    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    # Do the HTTP request
    response = requests.get(lookup_url, auth=(user, pwd), headers=headers )
    results = response.json()['result']
    return results
    

def create_incident(description, short_description, priority, caller):
    incident_url = 'https://dev79101.service-now.com/api/now/table/incident'
    user = snow_user
    pwd = snow_pw
    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    print(short_description)
    data = {
        'opened_by': caller,
        'short_description': short_description,
        'description': description,
        'priority': priority,
        'caller_id': caller,
        'comments': 'just testing the comments'
    }
    response = requests.post(incident_url, auth=(user, pwd), headers=headers, data=json.dumps(data))
    return response

class OpenIncidentForm(FormAction):

    def name(self) -> Text:
        return "open_incident_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return [
            "email",
            ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "email": self.from_entity(entity="email")
        }

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email is in ticket system."""

        caller = email_to_sysid(value)
        print(f"The results are: {caller}")

        if len(caller) == 1:
            # validation succeeded, set the value of the "email" slot to value
            return {"email": value}
        else:
            dispatcher.utter_template("utter_no_email", tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"email": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_incident_opened", tracker)
        return []