#!/usr/bin/env python
import json
import requests
import sys
import traceback


class PDIncident(object):

    __name__ = 'pd-incident'

    def __init__(self, service_key):
        self.service_key = service_key

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                print('an error occurred...')
                exc_type, exc_value, exc_traceback = sys.exc_info()
                self.trigger(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        return wrapped_func

    def trigger(self, desc):
        url = 'https://events.pagerduty.com/generic/2010-04-15/create_event.json'
        payload = json.dumps({
            "service_key": self.service_key,
            "event_type": "trigger",
            "description": desc,
        })
        try:
            req = requests.post(url, data=payload)
            if req.status_code == 200:
                print('an incident has been triggered in pagerduty...')
            else:
                print('there was a problem triggering an incident in pagerduty...')
        except requests.exceptions.ConnectionError:
            print('could not establish a connection to pagerduty...please check your internet connection...')

