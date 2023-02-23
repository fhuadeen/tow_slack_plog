import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from tow_slack_plog.slack_plog import SlackPlog
import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

webhook = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"


def test_slack_log():
    sp = SlackPlog(webhook)
    sp.setLevel(logging.DEBUG)
    logger.addHandler(sp)
    assert logger.debug("test slack logs") == None

def test_slack_plog_emit():
    sp = SlackPlog(webhook)
    # log = "<LogRecord: __main__, 10, /tow_slack_plog/tests/test_slack_plog.py, 15, 'test slack logs'>"
    # convert to LogRecord object
    log = logging.LogRecord(
        name="test_log",
        level=logging.DEBUG,
        pathname="/tow_slack_plog/tests/test_slack_plog.py",
        lineno=15,
        msg="test slack logs",
        args=("tester", "fhuad"),
        exc_info=BaseException,
    )

    res = sp.emit(log)
    assert res.status_code == 404
