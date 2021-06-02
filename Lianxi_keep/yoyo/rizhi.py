"""
nb-log 日志模块的基本使用
"""

from nb_log import LogManager

logger = LogManager('new').get_logger_and_add_handlers()

logger.info("hello")
logger.warning("this is warning")
logger.error("this error")
