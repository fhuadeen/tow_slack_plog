"""Main module for the Slack Plog package"""
import json
import logging
from urllib.parse import urlparse
from logging.handlers import HTTPHandler
from slack_sdk.webhook import WebhookClient


class SlackPlog(HTTPHandler):
    def __init__(self, slack_webhook_url):
        self.slack_webhook_url = slack_webhook_url
        parsed_url = urlparse(slack_webhook_url)
        HTTPHandler.__init__(self, parsed_url.netloc, parsed_url.path, method="POST", secure=True)

    # def mapLogRecord(self, record):

    #     # text = self.format(record)
    #     # payload = {
    #     #     'attachments': [
    #     #         text,
    #     #     ],
    #     # }

    #     # res = {
    #     #     'payload': json.dumps(payload),
    #     # }
    #     return res

    def emit(self, record):
        webhook = WebhookClient(self.slack_webhook_url)
        print('hook', webhook)

        try:
            res = webhook.send(text=str(record))
            print("res", res)
            return res
        except Exception as e:
            print("error", e)
            pass


class SlackFormatter(logging.Formatter):
    def format(self, record):
        ret = {}
        if record.levelname == 'INFO':
            ret['color'] = 'good'
        elif record.levelname == 'WARNING':
            ret['color'] = 'warning'
        elif record.levelname == 'ERROR':
            ret['color'] = '#E91E63'
        elif record.levelname == 'CRITICAL':
            ret['color'] = 'danger'

        ret['author_name'] = record.levelname
        ret['title'] = record.name
        ret['ts'] = record.created
        ret['text'] = super(SlackFormatter, self).format(record)
        return ret
