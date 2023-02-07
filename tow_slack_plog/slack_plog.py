"""Main module for the Slack Plog package"""
import json
import logging
from urllib.parse import urlparse
from logging.handlers import HTTPHandler


class SlackPlog(HTTPHandler):
    def __init__(self, slack_webhook_url):
        self.slack_webhook_url = slack_webhook_url
        parsed_url = urlparse(slack_webhook_url)
        HTTPHandler.__init__(self, parsed_url.netloc, parsed_url.path, method="POST", secure=True)
        print("Passed through")

    def mapLogRecord(self, record):
        text = self.format(record)
        payload = {
            'attachments': [
                text,
            ],
        }

        res = {
            'payload': json.dumps(payload),
        }
        print("pass mapping")
        return res