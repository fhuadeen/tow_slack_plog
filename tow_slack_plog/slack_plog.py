"""Main module for the Slack Plog package"""
import logging
from urllib.parse import urlparse
from logging.handlers import HTTPHandler
from slack_sdk.webhook import WebhookClient
from datetime import datetime


class SlackPlog(HTTPHandler):
    def __init__(self, slack_webhook_url):
        self.slack_webhook_url = slack_webhook_url
        parsed_url = urlparse(slack_webhook_url)
        # HTTPHandler.__init__(self, parsed_url.netloc, parsed_url.path, method="POST", secure=True)
        super().__init__(parsed_url.netloc, parsed_url.path, method="POST", secure=True)

    def emit(self, record):
        print('record:', record)
        print(type(record))
        map_record = self.mapLogRecord(record)
        created_at = datetime.fromtimestamp(map_record.get("created")).strftime("%Y-%m-%d %M:%s") # get the actual time
        log = f"{map_record.get('levelname')}:    {created_at} - {map_record.get('filename')} - {map_record.get('msg')} - lineno: {map_record.get('lineno')}"
        webhook = WebhookClient(self.slack_webhook_url)

        try:
            res = webhook.send(text=str(log))
            print("res status", res)
            return res
        except Exception as e:
            print("error", e)
            pass


# LOG_FORMAT = logging.Formatter("%(levelname)s:    %(asctime)s: %(module)s - %(message)s")
# webhook = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
# sp = SlackPlog(webhook)
# sp.setFormatter(LOG_FORMAT)
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(sp)
# logger.debug("test slack logs")
