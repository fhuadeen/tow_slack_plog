import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from tow_slack_plog.slack_plog import SlackPlog
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

wh = "https://hooks.slack.com/services/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"
sp = SlackPlog(wh)
sp.setLevel(logging.DEBUG)
logger.addHandler(sp)

logger.debug("test slack logs")
