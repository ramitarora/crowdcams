#__author__ = 'ramitarora'
from twilio.rest import TwilioRestClient


def send_sms():
    # Find these values at https://twilio.com/user/account
    account_sid = "ACa82d58b10b98a00c02062c3d8ee0d05c"
    auth_token = "c6e53c71ca63aa7d5a76a1e306861945"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+12176931197", from_="+12173963117",body="Crowdcams Alert: A motion was detected in one of the marked areas!")
