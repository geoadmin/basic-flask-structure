import logging
import logging.config
from os import path

import yaml

from flask import jsonify
from flask import make_response

from app.settings import ALLOWED_DOMAINS
from app.settings import LOGGING_CFG
from app.settings import LOGS_DIR

logger = logging.getLogger(__name__)

ALLOWED_DOMAINS_PATTERN = '({})'.format('|'.join(ALLOWED_DOMAINS))


def make_error_msg(code, msg):
    return make_response(jsonify({'success': False, 'error': {'code': code, 'message': msg}}), code)


def get_logging_cfg():
    print(f"LOGS_DIR is {LOGS_DIR}")
    print(f"LOGGING_CFG is {LOGGING_CFG}")

    config = {}
    with open(LOGGING_CFG, 'rt') as fd:
        config = yaml.safe_load(path.expandvars(fd.read()))

    logger.debug('Load logging configuration from file %s', LOGGING_CFG)
    return config


def init_logging():
    config = get_logging_cfg()
    logging.config.dictConfig(config)
