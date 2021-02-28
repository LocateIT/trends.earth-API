from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from gefapi.errors import EmailError
from sparkpost import SparkPost

#from flask import Flask
# from flask_mail import Mail, Message
#import os

#app = Flask(__name__)

#mail_settings = {
#    "MAIL_SERVER": 'smtp.gmail.com',
#    "MAIL_PORT": 465,
#    "MAIL_USE_TLS": False,
#    "MAIL_USE_SSL": True,
#    "MAIL_USERNAME": os.environ['EMAIL_USER'],
#    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
#}

#app.config.update(mail_settings)                                                                                                                                                                                
#mail = Mail(app)

class EmailService(object):
    """MailService Class"""

    @staticmethod
    def send_html_email(recipients=[], html='', from_email='info@promiseevents.co.ke', subject='[MISLAND] Undefined Subject'):
        try:

            #with app.app_context():
            #    response = Message(
            #        recipients = recipients,
            #        html = html,
            #        sender = sender,
            #        subject = subject
            #    )
            #    logging.info('{}'.format(response))
            #    mail.send(response)
            sp = SparkPost()
            response = sp.transmissions.send(
                recipients=recipients,
                html=html,
                from_email=from_email,
                subject=subject
            )
            return response
        except Exception as error:
            logging.error(error)
            raise EmailError(message=error)
