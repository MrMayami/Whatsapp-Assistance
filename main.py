from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# import os
# from twilio.rest import Client

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)


app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():

    incoming_msg = request.values.get('Body', '').lower()
    if incoming_msg:
        res = MessagingResponse()
        mMessage = res.message()
        mMessage.body(
            "Sorry, I'm still under development, check back later.\nTo get my latest update add *+2349039712085* on whatsapp and send DM *Status Update*.")

    return str(res)
