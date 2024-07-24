import re
from loguru import logger


def hide_sensitive_data(record):
    """
    Modify a log record to hide sensitive data.
    This function searches for specific patterns related to authorization,
    client ID, client secret, and password in a given log record and replaces
    the associated values with asterisks to mask the sensitive data
    """
    message = record["message"]
    message = re.sub(r'Authorization.*?,', '"Authorization": "********",', message)
    message = re.sub(r'"client_id": ".*?",', '"client_id": "********",', message)
    message = re.sub(r'"client_secret": ".*?"', '"client_secret": "********"', message)
    message = re.sub(r'"password": ".*?"', '"password": "********"', message)
    record["message"] = message
    return True


def setup_logger():
    log_format = ('<green>{time:YYYY-MM-DD HH:mm:ss.SSSSSS}</green> '
                  '| <level>{level: <8}</level> '
                  '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>')
    log_file = './reports/test_log.log'

    logger.remove()
    logger.add(sink=log_file, level='DEBUG', format=log_format, filter=hide_sensitive_data)

    return logger


log = setup_logger()

